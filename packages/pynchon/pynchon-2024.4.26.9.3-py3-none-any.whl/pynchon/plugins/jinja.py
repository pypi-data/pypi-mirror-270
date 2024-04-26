""" pynchon.plugins.jinja
"""

from fleks import tagging

from pynchon import abcs, api, cli

from pynchon.util import files, lme, text, typing  # noqa

LOGGER = lme.get_logger(__name__)

from pynchon.models.planner import RenderingPlugin  # noqa


@tagging.tags(click_aliases=["j"])
class Jinja(RenderingPlugin):
    """Renders files with {jinja.template_includes}"""

    # FIXME: diff-rendering with something like this:
    #   diff --color --minimal -w --side-by-side fname <(bash --pretty-print fname )

    class config_class(abcs.Config):
        config_key: typing.ClassVar[str] = "jinja"
        file_glob: str = typing.Field(
            default="*.j2", description="Where to find jinja templates"
        )
        template_includes: typing.List[str] = typing.Field(
            default=[],
            description="Where to find files for use with Jinja's `include` blocks",
        )
        exclude_patterns: typing.List[str] = typing.Field(
            description="File patterns to exclude from resource-listing"
        )
        vars: typing.Dict[str, str] = typing.Field(
            default={}, description="Extra variables for template rendering"
        )

        @property
        def exclude_patterns(self):
            "File patterns to exclude from resource-listing"
            from pynchon.config import globals

            global_ex = globals.exclude_patterns
            my_ex = self.__dict__.get("exclude_patterns", [])
            return list(set(global_ex + my_ex + ["**/pynchon/templates/includes/**"]))

    name = "jinja"
    priority = 7
    COMMAND_TEMPLATE = (
        "python -mpynchon.util.text render jinja "
        "{src} --context-file {context_file} "
        "--output {output} {template_args}"
    )

    def _get_jinja_context(self):
        """ """
        if getattr(self, "_jinja_ctx_file", None):
            return self._jinja_ctx_file
        else:
            fname = ".tmp.jinja.ctx.json"
            with open(fname, "w") as fhandle:
                fhandle.write(text.to_json(self.project_config))
            self._jinja_ctx_file = fname
            return fname

    @property
    def _include_folders(self):
        includes = self.project_config.jinja["template_includes"]
        from pynchon import api

        includes = api.render.get_jinja_includes(*includes)
        return includes

    @cli.click.flag("--local")
    def list_includes(
        self,
        local: bool = False,
    ):
        """Lists full path of each include-file"""
        includes = self._include_folders
        if local:
            includes.remove(api.render.PYNCHON_CORE_INCLUDES)
        includes = [abcs.Path(t) / "**" / self.config.file_glob for t in includes]
        LOGGER.warning(includes)
        matches = files.find_globs(includes)
        return matches

    @cli.click.flag("--local")
    def list_include_args(
        self,
        local: bool = False,
    ):
        """
        Lists all usable {% include ... %} values
        """
        includes = self.list_includes(local=local)
        out = []
        for fname in includes:
            fname = abcs.Path(fname)
            for inc in self._include_folders:
                try:
                    fname = fname.relative_to(inc)
                except ValueError:
                    continue
                else:
                    out.append(fname)
                break
            else:
                pass
        return out

    @tagging.tags(click_aliases=["ls"])
    def list(self, changes=False, **kwargs):
        """
        Lists affected resources for this project
        """
        return self._list(changes=changes, **kwargs)

    @cli.click.argument("files", nargs=-1)
    def render(self, files, plan_only: bool = False):
        """Renders 1 or more jinja templates"""
        files = [abcs.Path(file) for file in files]
        jctx = self._get_jinja_context()
        templates = self._get_template_args()
        plan = super(self.__class__, self).plan()
        for src in files:
            assert src.exists()
            output = str(src).replace(".j2", "")
            assert output != str(src), "filename did not change!"
            plan.append(
                self.goal(
                    type="render",
                    resource=output,
                    command=self.COMMAND_TEMPLATE.format(
                        src=src,
                        context_file=jctx,
                        template_args=templates,
                        output=output,
                    ),
                )
            )
        if plan_only:
            return plan
        else:
            return plan.apply(strict=True, fail_fast=True)

    def _get_template_args(self):
        """ """
        # import IPython; IPython.embed()
        templates = self["template_includes"]
        templates = [t for t in templates]
        templates = [f"--include {t}" for t in templates]
        templates = " ".join(templates)
        return templates

    def plan(
        self,
        config=None,
    ) -> typing.List:
        """Creates a plan for this plugin"""

        plan = super(self.__class__, self).plan()
        jctx = self._get_jinja_context()
        templates = self._get_template_args()
        for src in self.list():
            output = str(src).replace(".j2", "")
            plan.append(
                self.goal(
                    type="render",
                    resource=output,
                    command=self.COMMAND_TEMPLATE.format(
                        src=src,
                        context_file=jctx,
                        template_args=templates,
                        output=output,
                    ),
                )
            )
        return plan.finalize()
