import mkdocs.plugins
from mkdocs.config import config_options

class SampleMkDocsPlugin(mkdocs.plugins.BasePlugin):
    """
    Sample MkDocs plugin to add custom text to the markdown pages,
    with an option to underline the text. This version also demonstrates 
    knowledge of available hooks by overriding all of them.
    """
    config_scheme = (
        ('text', config_options.Type(str, default='Default text')),
        ('underline', config_options.Type(bool, default=False)),
    )

    def on_config(self, config):
        """
        Override of on_config hook.
        """
        pass

    def on_pre_build(self, config):
        """
        Override of on_pre_build hook.
        """
        pass

    def on_files(self, files, config):
        """
        Override of on_files hook.
        """
        pass

    def on_nav(self, nav, config, files):
        """
        Override of on_nav hook.
        """
        pass

    def on_env(self, env, config, files):
        """
        Override of on_env hook.
        """
        pass

    def on_pre_template(self, template, template_name, config):
        """
        Override of on_pre_template hook.
        """
        pass

    def on_template_context(self, context, template_name, config):
        """
        Override of on_template_context hook.
        """
        pass

    def on_page_content(self, html, page, config, files):
        """
        Override of on_page_content hook.
        """
        pass

    def on_page_context(self, context, page, config, nav):
        """
        Override of on_page_context hook.
        """
        pass

    def on_post_template(self, output_content, template_name, config):
        """
        Override of on_post_template hook.
        """
        pass

    def on_post_build(self, config):
        """
        Override of on_post_build hook.
        """
        pass

    def on_serve(self, server, config, builder):
        """
        Override of on_serve hook, applicable when using the `mkdocs serve` command.
        """
        pass

    def on_build_error(self, error):
        """
        Override of on_build_error hook.
        """
        pass

    def on_page_markdown(self, markdown, page=None, config=None, site_navigation=None, **kwargs):
        """
        Hook to modify the Markdown text of each page. Adds specified text,
        optionally underlined, at the end of the page content.

        :param markdown: The original markdown content of the page.
        :param page: The page object (unused in this example).
        :param config: The site config (unused in this example).
        :param site_navigation: The site navigation object (unused in this example).
        :return: Modified markdown content.
        """
        # Decide if the text should be underlined
        text_to_add = f"<u>{self.config['text']}</u>" if self.config['underline'] else self.config['text']
        # Ensure clear separation from existing content
        return markdown + f"\n\n<!-- Custom Plugin Content -->\n{text_to_add}"
