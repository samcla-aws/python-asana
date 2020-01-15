# coding=utf-8
class _CustomFieldSettings:

    def __init__(self, client=None):
        self.client = client

    def add_custom_field_setting_for_portfolio(self, portfolio_gid, params={}, **options):
        """Add a custom field to a portfolio
        :param str portfolio_gid: (required) Globally unique identifier for the portfolio.
        :param Object params: Parameters for the request
        :return: Object
        """
        path = "/portfolios/{portfolio_gid}/addCustomFieldSetting".replace("{portfolio_gid}", portfolio_gid)
        return self.client.get(path, params, **options)


    def get_custom_field_settings_for_portfolio(self, portfolio_gid, params={}, **options):
        """Get a portfolio's custom fields
        :param str portfolio_gid: (required) Globally unique identifier for the portfolio.
        :param Object params: Parameters for the request
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        path = "/portfolios/{portfolio_gid}/custom_field_settings".replace("{portfolio_gid}", portfolio_gid)
        return self.client.get(path, params, **options)


    def get_custom_field_settings_for_project(self, project_gid, params={}, **options):
        """Get a project's custom fields
        :param str project_gid: (required) Globally unique identifier for the project.
        :param Object params: Parameters for the request
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        path = "/projects/{project_gid}/custom_field_settings".replace("{project_gid}", project_gid)
        return self.client.get(path, params, **options)


    def remove_custom_field_setting_for_portfolio(self, portfolio_gid, params={}, **options):
        """Remove a custom field from a portfolio
        :param str portfolio_gid: (required) Globally unique identifier for the portfolio.
        :param Object params: Parameters for the request
        :return: Object
        """
        path = "/portfolios/{portfolio_gid}/removeCustomFieldSetting".replace("{portfolio_gid}", portfolio_gid)
        return self.client.get(path, params, **options)

