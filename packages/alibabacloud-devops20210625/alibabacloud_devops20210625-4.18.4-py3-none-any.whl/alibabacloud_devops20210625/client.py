# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_devops20210625 import models as devops_20210625_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('devops', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_group_member_with_options(
        self,
        group_id: str,
        request: devops_20210625_models.AddGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.AddGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.access_level):
            body['accessLevel'] = request.access_level
        if not UtilClient.is_unset(request.aliyun_pks):
            body['aliyunPks'] = request.aliyun_pks
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddGroupMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/groups/{OpenApiUtilClient.get_encode_param(group_id)}/members/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.AddGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_group_member_with_options_async(
        self,
        group_id: str,
        request: devops_20210625_models.AddGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.AddGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.access_level):
            body['accessLevel'] = request.access_level
        if not UtilClient.is_unset(request.aliyun_pks):
            body['aliyunPks'] = request.aliyun_pks
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddGroupMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/groups/{OpenApiUtilClient.get_encode_param(group_id)}/members/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.AddGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_group_member(
        self,
        group_id: str,
        request: devops_20210625_models.AddGroupMemberRequest,
    ) -> devops_20210625_models.AddGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_group_member_with_options(group_id, request, headers, runtime)

    async def add_group_member_async(
        self,
        group_id: str,
        request: devops_20210625_models.AddGroupMemberRequest,
    ) -> devops_20210625_models.AddGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_group_member_with_options_async(group_id, request, headers, runtime)

    def add_pipeline_relations_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.AddPipelineRelationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.AddPipelineRelationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rel_object_ids):
            query['relObjectIds'] = request.rel_object_ids
        if not UtilClient.is_unset(request.rel_object_type):
            query['relObjectType'] = request.rel_object_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPipelineRelations',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRelations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.AddPipelineRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_pipeline_relations_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.AddPipelineRelationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.AddPipelineRelationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rel_object_ids):
            query['relObjectIds'] = request.rel_object_ids
        if not UtilClient.is_unset(request.rel_object_type):
            query['relObjectType'] = request.rel_object_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPipelineRelations',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRelations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.AddPipelineRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_pipeline_relations(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.AddPipelineRelationsRequest,
    ) -> devops_20210625_models.AddPipelineRelationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_pipeline_relations_with_options(organization_id, pipeline_id, request, headers, runtime)

    async def add_pipeline_relations_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.AddPipelineRelationsRequest,
    ) -> devops_20210625_models.AddPipelineRelationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_pipeline_relations_with_options_async(organization_id, pipeline_id, request, headers, runtime)

    def add_repository_member_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.AddRepositoryMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.AddRepositoryMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.access_level):
            body['accessLevel'] = request.access_level
        if not UtilClient.is_unset(request.aliyun_pks):
            body['aliyunPks'] = request.aliyun_pks
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddRepositoryMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.AddRepositoryMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_repository_member_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.AddRepositoryMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.AddRepositoryMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.access_level):
            body['accessLevel'] = request.access_level
        if not UtilClient.is_unset(request.aliyun_pks):
            body['aliyunPks'] = request.aliyun_pks
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddRepositoryMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.AddRepositoryMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_repository_member(
        self,
        repository_id: str,
        request: devops_20210625_models.AddRepositoryMemberRequest,
    ) -> devops_20210625_models.AddRepositoryMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_repository_member_with_options(repository_id, request, headers, runtime)

    async def add_repository_member_async(
        self,
        repository_id: str,
        request: devops_20210625_models.AddRepositoryMemberRequest,
    ) -> devops_20210625_models.AddRepositoryMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_repository_member_with_options_async(repository_id, request, headers, runtime)

    def add_webhook_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.AddWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.AddWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.enable_ssl_verification):
            body['enableSslVerification'] = request.enable_ssl_verification
        if not UtilClient.is_unset(request.merge_requests_events):
            body['mergeRequestsEvents'] = request.merge_requests_events
        if not UtilClient.is_unset(request.note_events):
            body['noteEvents'] = request.note_events
        if not UtilClient.is_unset(request.push_events):
            body['pushEvents'] = request.push_events
        if not UtilClient.is_unset(request.secret_token):
            body['secretToken'] = request.secret_token
        if not UtilClient.is_unset(request.tag_push_events):
            body['tagPushEvents'] = request.tag_push_events
        if not UtilClient.is_unset(request.url):
            body['url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddWebhook',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/webhooks/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.AddWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_webhook_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.AddWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.AddWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.enable_ssl_verification):
            body['enableSslVerification'] = request.enable_ssl_verification
        if not UtilClient.is_unset(request.merge_requests_events):
            body['mergeRequestsEvents'] = request.merge_requests_events
        if not UtilClient.is_unset(request.note_events):
            body['noteEvents'] = request.note_events
        if not UtilClient.is_unset(request.push_events):
            body['pushEvents'] = request.push_events
        if not UtilClient.is_unset(request.secret_token):
            body['secretToken'] = request.secret_token
        if not UtilClient.is_unset(request.tag_push_events):
            body['tagPushEvents'] = request.tag_push_events
        if not UtilClient.is_unset(request.url):
            body['url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddWebhook',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/webhooks/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.AddWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_webhook(
        self,
        repository_id: str,
        request: devops_20210625_models.AddWebhookRequest,
    ) -> devops_20210625_models.AddWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_webhook_with_options(repository_id, request, headers, runtime)

    async def add_webhook_async(
        self,
        repository_id: str,
        request: devops_20210625_models.AddWebhookRequest,
    ) -> devops_20210625_models.AddWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_webhook_with_options_async(repository_id, request, headers, runtime)

    def close_merge_request_with_options(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.CloseMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CloseMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseMergeRequest',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/merge_requests/{OpenApiUtilClient.get_encode_param(local_id)}/close',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CloseMergeRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_merge_request_with_options_async(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.CloseMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CloseMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseMergeRequest',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/merge_requests/{OpenApiUtilClient.get_encode_param(local_id)}/close',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CloseMergeRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_merge_request(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.CloseMergeRequestRequest,
    ) -> devops_20210625_models.CloseMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.close_merge_request_with_options(repository_id, local_id, request, headers, runtime)

    async def close_merge_request_async(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.CloseMergeRequestRequest,
    ) -> devops_20210625_models.CloseMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.close_merge_request_with_options_async(repository_id, local_id, request, headers, runtime)

    def create_app_members_with_options(
        self,
        app_name: str,
        request: devops_20210625_models.CreateAppMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateAppMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.player_list):
            body['playerList'] = request.player_list
        if not UtilClient.is_unset(request.role_names):
            body['roleNames'] = request.role_names
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAppMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/appstack/apps/{OpenApiUtilClient.get_encode_param(app_name)}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateAppMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_members_with_options_async(
        self,
        app_name: str,
        request: devops_20210625_models.CreateAppMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateAppMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.player_list):
            body['playerList'] = request.player_list
        if not UtilClient.is_unset(request.role_names):
            body['roleNames'] = request.role_names
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAppMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/appstack/apps/{OpenApiUtilClient.get_encode_param(app_name)}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateAppMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_members(
        self,
        app_name: str,
        request: devops_20210625_models.CreateAppMembersRequest,
    ) -> devops_20210625_models.CreateAppMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_app_members_with_options(app_name, request, headers, runtime)

    async def create_app_members_async(
        self,
        app_name: str,
        request: devops_20210625_models.CreateAppMembersRequest,
    ) -> devops_20210625_models.CreateAppMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_app_members_with_options_async(app_name, request, headers, runtime)

    def create_branch_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.branch_name):
            body['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.ref):
            body['ref'] = request.ref
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBranch',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/branches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateBranchResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_branch_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.branch_name):
            body['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.ref):
            body['ref'] = request.ref
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBranch',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/branches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateBranchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_branch(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateBranchRequest,
    ) -> devops_20210625_models.CreateBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_branch_with_options(repository_id, request, headers, runtime)

    async def create_branch_async(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateBranchRequest,
    ) -> devops_20210625_models.CreateBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_branch_with_options_async(repository_id, request, headers, runtime)

    def create_check_run_with_options(
        self,
        request: devops_20210625_models.CreateCheckRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateCheckRunResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        body = {}
        if not UtilClient.is_unset(request.annotations):
            body['annotations'] = request.annotations
        if not UtilClient.is_unset(request.completed_at):
            body['completedAt'] = request.completed_at
        if not UtilClient.is_unset(request.conclusion):
            body['conclusion'] = request.conclusion
        if not UtilClient.is_unset(request.details_url):
            body['detailsUrl'] = request.details_url
        if not UtilClient.is_unset(request.external_id):
            body['externalId'] = request.external_id
        if not UtilClient.is_unset(request.head_sha):
            body['headSha'] = request.head_sha
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.output):
            body['output'] = request.output
        if not UtilClient.is_unset(request.started_at):
            body['startedAt'] = request.started_at
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCheckRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/check_runs/create_check_run',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateCheckRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_check_run_with_options_async(
        self,
        request: devops_20210625_models.CreateCheckRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateCheckRunResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        body = {}
        if not UtilClient.is_unset(request.annotations):
            body['annotations'] = request.annotations
        if not UtilClient.is_unset(request.completed_at):
            body['completedAt'] = request.completed_at
        if not UtilClient.is_unset(request.conclusion):
            body['conclusion'] = request.conclusion
        if not UtilClient.is_unset(request.details_url):
            body['detailsUrl'] = request.details_url
        if not UtilClient.is_unset(request.external_id):
            body['externalId'] = request.external_id
        if not UtilClient.is_unset(request.head_sha):
            body['headSha'] = request.head_sha
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.output):
            body['output'] = request.output
        if not UtilClient.is_unset(request.started_at):
            body['startedAt'] = request.started_at
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCheckRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/check_runs/create_check_run',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateCheckRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_check_run(
        self,
        request: devops_20210625_models.CreateCheckRunRequest,
    ) -> devops_20210625_models.CreateCheckRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_check_run_with_options(request, headers, runtime)

    async def create_check_run_async(
        self,
        request: devops_20210625_models.CreateCheckRunRequest,
    ) -> devops_20210625_models.CreateCheckRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_check_run_with_options_async(request, headers, runtime)

    def create_comment_with_options(
        self,
        request: devops_20210625_models.CreateCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateCommentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.local_id):
            query['localId'] = request.local_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        body = {}
        if not UtilClient.is_unset(request.comment_type):
            body['commentType'] = request.comment_type
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.draft):
            body['draft'] = request.draft
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        if not UtilClient.is_unset(request.line_number):
            body['lineNumber'] = request.line_number
        if not UtilClient.is_unset(request.parent_comment_biz_id):
            body['parentCommentBizId'] = request.parent_comment_biz_id
        if not UtilClient.is_unset(request.patch_set_biz_id):
            body['patchSetBizId'] = request.patch_set_biz_id
        if not UtilClient.is_unset(request.resolved):
            body['resolved'] = request.resolved
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/code_reviews/comments/create_comment',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateCommentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_comment_with_options_async(
        self,
        request: devops_20210625_models.CreateCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateCommentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.local_id):
            query['localId'] = request.local_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        body = {}
        if not UtilClient.is_unset(request.comment_type):
            body['commentType'] = request.comment_type
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.draft):
            body['draft'] = request.draft
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        if not UtilClient.is_unset(request.line_number):
            body['lineNumber'] = request.line_number
        if not UtilClient.is_unset(request.parent_comment_biz_id):
            body['parentCommentBizId'] = request.parent_comment_biz_id
        if not UtilClient.is_unset(request.patch_set_biz_id):
            body['patchSetBizId'] = request.patch_set_biz_id
        if not UtilClient.is_unset(request.resolved):
            body['resolved'] = request.resolved
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/code_reviews/comments/create_comment',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateCommentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_comment(
        self,
        request: devops_20210625_models.CreateCommentRequest,
    ) -> devops_20210625_models.CreateCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_comment_with_options(request, headers, runtime)

    async def create_comment_async(
        self,
        request: devops_20210625_models.CreateCommentRequest,
    ) -> devops_20210625_models.CreateCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_comment_with_options_async(request, headers, runtime)

    def create_commit_status_with_options(
        self,
        request: devops_20210625_models.CreateCommitStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateCommitStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        if not UtilClient.is_unset(request.sha):
            query['sha'] = request.sha
        body = {}
        if not UtilClient.is_unset(request.context):
            body['context'] = request.context
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.state):
            body['state'] = request.state
        if not UtilClient.is_unset(request.target_url):
            body['targetUrl'] = request.target_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCommitStatus',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/repository/commit_statuses/create_commit_status',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateCommitStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_commit_status_with_options_async(
        self,
        request: devops_20210625_models.CreateCommitStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateCommitStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        if not UtilClient.is_unset(request.sha):
            query['sha'] = request.sha
        body = {}
        if not UtilClient.is_unset(request.context):
            body['context'] = request.context
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.state):
            body['state'] = request.state
        if not UtilClient.is_unset(request.target_url):
            body['targetUrl'] = request.target_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCommitStatus',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/repository/commit_statuses/create_commit_status',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateCommitStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_commit_status(
        self,
        request: devops_20210625_models.CreateCommitStatusRequest,
    ) -> devops_20210625_models.CreateCommitStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_commit_status_with_options(request, headers, runtime)

    async def create_commit_status_async(
        self,
        request: devops_20210625_models.CreateCommitStatusRequest,
    ) -> devops_20210625_models.CreateCommitStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_commit_status_with_options_async(request, headers, runtime)

    def create_commit_with_multiple_files_with_options(
        self,
        request: devops_20210625_models.CreateCommitWithMultipleFilesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateCommitWithMultipleFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        body = {}
        if not UtilClient.is_unset(request.actions):
            body['actions'] = request.actions
        if not UtilClient.is_unset(request.branch):
            body['branch'] = request.branch
        if not UtilClient.is_unset(request.commit_message):
            body['commitMessage'] = request.commit_message
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCommitWithMultipleFiles',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/repository/commits/files',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateCommitWithMultipleFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_commit_with_multiple_files_with_options_async(
        self,
        request: devops_20210625_models.CreateCommitWithMultipleFilesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateCommitWithMultipleFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        body = {}
        if not UtilClient.is_unset(request.actions):
            body['actions'] = request.actions
        if not UtilClient.is_unset(request.branch):
            body['branch'] = request.branch
        if not UtilClient.is_unset(request.commit_message):
            body['commitMessage'] = request.commit_message
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCommitWithMultipleFiles',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/repository/commits/files',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateCommitWithMultipleFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_commit_with_multiple_files(
        self,
        request: devops_20210625_models.CreateCommitWithMultipleFilesRequest,
    ) -> devops_20210625_models.CreateCommitWithMultipleFilesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_commit_with_multiple_files_with_options(request, headers, runtime)

    async def create_commit_with_multiple_files_async(
        self,
        request: devops_20210625_models.CreateCommitWithMultipleFilesRequest,
    ) -> devops_20210625_models.CreateCommitWithMultipleFilesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_commit_with_multiple_files_with_options_async(request, headers, runtime)

    def create_deploy_key_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateDeployKeyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateDeployKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.key):
            body['key'] = request.key
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDeployKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/keys/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateDeployKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_deploy_key_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateDeployKeyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateDeployKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.key):
            body['key'] = request.key
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDeployKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/keys/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateDeployKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_deploy_key(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateDeployKeyRequest,
    ) -> devops_20210625_models.CreateDeployKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_deploy_key_with_options(repository_id, request, headers, runtime)

    async def create_deploy_key_async(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateDeployKeyRequest,
    ) -> devops_20210625_models.CreateDeployKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_deploy_key_with_options_async(repository_id, request, headers, runtime)

    def create_file_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.branch_name):
            body['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.commit_message):
            body['commitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.encoding):
            body['encoding'] = request.encoding
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFile',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_file_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.branch_name):
            body['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.commit_message):
            body['commitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.encoding):
            body['encoding'] = request.encoding
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFile',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_file(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateFileRequest,
    ) -> devops_20210625_models.CreateFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_file_with_options(repository_id, request, headers, runtime)

    async def create_file_async(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateFileRequest,
    ) -> devops_20210625_models.CreateFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_file_with_options_async(repository_id, request, headers, runtime)

    def create_flow_tag_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateFlowTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.color):
            query['color'] = request.color
        if not UtilClient.is_unset(request.flow_tag_group_id):
            query['flowTagGroupId'] = request.flow_tag_group_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateFlowTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_tag_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateFlowTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.color):
            query['color'] = request.color
        if not UtilClient.is_unset(request.flow_tag_group_id):
            query['flowTagGroupId'] = request.flow_tag_group_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateFlowTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow_tag(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagRequest,
    ) -> devops_20210625_models.CreateFlowTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_flow_tag_with_options(organization_id, request, headers, runtime)

    async def create_flow_tag_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagRequest,
    ) -> devops_20210625_models.CreateFlowTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_flow_tag_with_options_async(organization_id, request, headers, runtime)

    def create_flow_tag_group_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateFlowTagGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tagGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateFlowTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_tag_group_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateFlowTagGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tagGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateFlowTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow_tag_group(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagGroupRequest,
    ) -> devops_20210625_models.CreateFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_flow_tag_group_with_options(organization_id, request, headers, runtime)

    async def create_flow_tag_group_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagGroupRequest,
    ) -> devops_20210625_models.CreateFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_flow_tag_group_with_options_async(organization_id, request, headers, runtime)

    def create_host_group_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateHostGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateHostGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_region):
            body['aliyunRegion'] = request.aliyun_region
        if not UtilClient.is_unset(request.ecs_label_key):
            body['ecsLabelKey'] = request.ecs_label_key
        if not UtilClient.is_unset(request.ecs_label_value):
            body['ecsLabelValue'] = request.ecs_label_value
        if not UtilClient.is_unset(request.ecs_type):
            body['ecsType'] = request.ecs_type
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.machine_infos):
            body['machineInfos'] = request.machine_infos
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.service_connection_id):
            body['serviceConnectionId'] = request.service_connection_id
        if not UtilClient.is_unset(request.tag_ids):
            body['tagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/hostGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_host_group_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateHostGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateHostGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_region):
            body['aliyunRegion'] = request.aliyun_region
        if not UtilClient.is_unset(request.ecs_label_key):
            body['ecsLabelKey'] = request.ecs_label_key
        if not UtilClient.is_unset(request.ecs_label_value):
            body['ecsLabelValue'] = request.ecs_label_value
        if not UtilClient.is_unset(request.ecs_type):
            body['ecsType'] = request.ecs_type
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.machine_infos):
            body['machineInfos'] = request.machine_infos
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.service_connection_id):
            body['serviceConnectionId'] = request.service_connection_id
        if not UtilClient.is_unset(request.tag_ids):
            body['tagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/hostGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_host_group(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateHostGroupRequest,
    ) -> devops_20210625_models.CreateHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_host_group_with_options(organization_id, request, headers, runtime)

    async def create_host_group_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateHostGroupRequest,
    ) -> devops_20210625_models.CreateHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_host_group_with_options_async(organization_id, request, headers, runtime)

    def create_merge_request_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.create_from):
            body['createFrom'] = request.create_from
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.reviewer_ids):
            body['reviewerIds'] = request.reviewer_ids
        if not UtilClient.is_unset(request.source_branch):
            body['sourceBranch'] = request.source_branch
        if not UtilClient.is_unset(request.source_project_id):
            body['sourceProjectId'] = request.source_project_id
        if not UtilClient.is_unset(request.target_branch):
            body['targetBranch'] = request.target_branch
        if not UtilClient.is_unset(request.target_project_id):
            body['targetProjectId'] = request.target_project_id
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        if not UtilClient.is_unset(request.work_item_ids):
            body['workItemIds'] = request.work_item_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMergeRequest',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/merge_requests',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateMergeRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_merge_request_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.create_from):
            body['createFrom'] = request.create_from
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.reviewer_ids):
            body['reviewerIds'] = request.reviewer_ids
        if not UtilClient.is_unset(request.source_branch):
            body['sourceBranch'] = request.source_branch
        if not UtilClient.is_unset(request.source_project_id):
            body['sourceProjectId'] = request.source_project_id
        if not UtilClient.is_unset(request.target_branch):
            body['targetBranch'] = request.target_branch
        if not UtilClient.is_unset(request.target_project_id):
            body['targetProjectId'] = request.target_project_id
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        if not UtilClient.is_unset(request.work_item_ids):
            body['workItemIds'] = request.work_item_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMergeRequest',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/merge_requests',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateMergeRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_merge_request(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateMergeRequestRequest,
    ) -> devops_20210625_models.CreateMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_merge_request_with_options(repository_id, request, headers, runtime)

    async def create_merge_request_async(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateMergeRequestRequest,
    ) -> devops_20210625_models.CreateMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_merge_request_with_options_async(repository_id, request, headers, runtime)

    def create_oauth_token_with_options(
        self,
        request: devops_20210625_models.CreateOAuthTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateOAuthTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.client_secret):
            body['clientSecret'] = request.client_secret
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.grant_type):
            body['grantType'] = request.grant_type
        if not UtilClient.is_unset(request.login):
            body['login'] = request.login
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOAuthToken',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/login/oauth/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateOAuthTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_oauth_token_with_options_async(
        self,
        request: devops_20210625_models.CreateOAuthTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateOAuthTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.client_secret):
            body['clientSecret'] = request.client_secret
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.grant_type):
            body['grantType'] = request.grant_type
        if not UtilClient.is_unset(request.login):
            body['login'] = request.login
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOAuthToken',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/login/oauth/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateOAuthTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_oauth_token(
        self,
        request: devops_20210625_models.CreateOAuthTokenRequest,
    ) -> devops_20210625_models.CreateOAuthTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_oauth_token_with_options(request, headers, runtime)

    async def create_oauth_token_async(
        self,
        request: devops_20210625_models.CreateOAuthTokenRequest,
    ) -> devops_20210625_models.CreateOAuthTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_oauth_token_with_options_async(request, headers, runtime)

    def create_pipeline_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreatePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreatePipelineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreatePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreatePipelineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreatePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipeline(
        self,
        organization_id: str,
        request: devops_20210625_models.CreatePipelineRequest,
    ) -> devops_20210625_models.CreatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipeline_with_options(organization_id, request, headers, runtime)

    async def create_pipeline_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreatePipelineRequest,
    ) -> devops_20210625_models.CreatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_pipeline_with_options_async(organization_id, request, headers, runtime)

    def create_pipeline_group_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreatePipelineGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreatePipelineGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreatePipelineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_group_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreatePipelineGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreatePipelineGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreatePipelineGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipeline_group(
        self,
        organization_id: str,
        request: devops_20210625_models.CreatePipelineGroupRequest,
    ) -> devops_20210625_models.CreatePipelineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipeline_group_with_options(organization_id, request, headers, runtime)

    async def create_pipeline_group_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreatePipelineGroupRequest,
    ) -> devops_20210625_models.CreatePipelineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_pipeline_group_with_options_async(organization_id, request, headers, runtime)

    def create_project_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_code):
            body['customCode'] = request.custom_code
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.template_identifier):
            body['templateIdentifier'] = request.template_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/createProject',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_code):
            body['customCode'] = request.custom_code
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.template_identifier):
            body['templateIdentifier'] = request.template_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/createProject',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateProjectRequest,
    ) -> devops_20210625_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(organization_id, request, headers, runtime)

    async def create_project_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateProjectRequest,
    ) -> devops_20210625_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_project_with_options_async(organization_id, request, headers, runtime)

    def create_project_label_with_options(
        self,
        request: devops_20210625_models.CreateProjectLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateProjectLabelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        body = {}
        if not UtilClient.is_unset(request.color):
            body['color'] = request.color
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProjectLabel',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/labels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateProjectLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_label_with_options_async(
        self,
        request: devops_20210625_models.CreateProjectLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateProjectLabelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        body = {}
        if not UtilClient.is_unset(request.color):
            body['color'] = request.color
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProjectLabel',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/labels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateProjectLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project_label(
        self,
        request: devops_20210625_models.CreateProjectLabelRequest,
    ) -> devops_20210625_models.CreateProjectLabelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_label_with_options(request, headers, runtime)

    async def create_project_label_async(
        self,
        request: devops_20210625_models.CreateProjectLabelRequest,
    ) -> devops_20210625_models.CreateProjectLabelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_project_label_with_options_async(request, headers, runtime)

    def create_protectd_branch_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateProtectdBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateProtectdBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.allow_merge_roles):
            body['allowMergeRoles'] = request.allow_merge_roles
        if not UtilClient.is_unset(request.allow_merge_user_ids):
            body['allowMergeUserIds'] = request.allow_merge_user_ids
        if not UtilClient.is_unset(request.allow_push_roles):
            body['allowPushRoles'] = request.allow_push_roles
        if not UtilClient.is_unset(request.allow_push_user_ids):
            body['allowPushUserIds'] = request.allow_push_user_ids
        if not UtilClient.is_unset(request.branch):
            body['branch'] = request.branch
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.merge_request_setting):
            body['mergeRequestSetting'] = request.merge_request_setting
        if not UtilClient.is_unset(request.test_setting_dto):
            body['testSettingDTO'] = request.test_setting_dto
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProtectdBranch',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/protect_branches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateProtectdBranchResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_protectd_branch_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateProtectdBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateProtectdBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.allow_merge_roles):
            body['allowMergeRoles'] = request.allow_merge_roles
        if not UtilClient.is_unset(request.allow_merge_user_ids):
            body['allowMergeUserIds'] = request.allow_merge_user_ids
        if not UtilClient.is_unset(request.allow_push_roles):
            body['allowPushRoles'] = request.allow_push_roles
        if not UtilClient.is_unset(request.allow_push_user_ids):
            body['allowPushUserIds'] = request.allow_push_user_ids
        if not UtilClient.is_unset(request.branch):
            body['branch'] = request.branch
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.merge_request_setting):
            body['mergeRequestSetting'] = request.merge_request_setting
        if not UtilClient.is_unset(request.test_setting_dto):
            body['testSettingDTO'] = request.test_setting_dto
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProtectdBranch',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/protect_branches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateProtectdBranchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_protectd_branch(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateProtectdBranchRequest,
    ) -> devops_20210625_models.CreateProtectdBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_protectd_branch_with_options(repository_id, request, headers, runtime)

    async def create_protectd_branch_async(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateProtectdBranchRequest,
    ) -> devops_20210625_models.CreateProtectdBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_protectd_branch_with_options_async(repository_id, request, headers, runtime)

    def create_push_rule_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.CreatePushRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreatePushRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.rule_infos):
            body['ruleInfos'] = request.rule_infos
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePushRule',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/push_rule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreatePushRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_push_rule_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.CreatePushRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreatePushRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.rule_infos):
            body['ruleInfos'] = request.rule_infos
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePushRule',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/push_rule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreatePushRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_push_rule(
        self,
        repository_id: str,
        request: devops_20210625_models.CreatePushRuleRequest,
    ) -> devops_20210625_models.CreatePushRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_push_rule_with_options(repository_id, request, headers, runtime)

    async def create_push_rule_async(
        self,
        repository_id: str,
        request: devops_20210625_models.CreatePushRuleRequest,
    ) -> devops_20210625_models.CreatePushRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_push_rule_with_options_async(repository_id, request, headers, runtime)

    def create_repository_with_options(
        self,
        request: devops_20210625_models.CreateRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.create_parent_path):
            query['createParentPath'] = request.create_parent_path
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sync):
            query['sync'] = request.sync
        body = {}
        if not UtilClient.is_unset(request.avatar_url):
            body['avatarUrl'] = request.avatar_url
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.gitignore_type):
            body['gitignoreType'] = request.gitignore_type
        if not UtilClient.is_unset(request.import_account):
            body['importAccount'] = request.import_account
        if not UtilClient.is_unset(request.import_demo_project):
            body['importDemoProject'] = request.import_demo_project
        if not UtilClient.is_unset(request.import_repo_type):
            body['importRepoType'] = request.import_repo_type
        if not UtilClient.is_unset(request.import_token):
            body['importToken'] = request.import_token
        if not UtilClient.is_unset(request.import_token_encrypted):
            body['importTokenEncrypted'] = request.import_token_encrypted
        if not UtilClient.is_unset(request.import_url):
            body['importUrl'] = request.import_url
        if not UtilClient.is_unset(request.init_standard_service):
            body['initStandardService'] = request.init_standard_service
        if not UtilClient.is_unset(request.is_crypto_enabled):
            body['isCryptoEnabled'] = request.is_crypto_enabled
        if not UtilClient.is_unset(request.local_import_url):
            body['localImportUrl'] = request.local_import_url
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.namespace_id):
            body['namespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.path):
            body['path'] = request.path
        if not UtilClient.is_unset(request.readme_type):
            body['readmeType'] = request.readme_type
        if not UtilClient.is_unset(request.visibility_level):
            body['visibilityLevel'] = request.visibility_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repository_with_options_async(
        self,
        request: devops_20210625_models.CreateRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.create_parent_path):
            query['createParentPath'] = request.create_parent_path
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sync):
            query['sync'] = request.sync
        body = {}
        if not UtilClient.is_unset(request.avatar_url):
            body['avatarUrl'] = request.avatar_url
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.gitignore_type):
            body['gitignoreType'] = request.gitignore_type
        if not UtilClient.is_unset(request.import_account):
            body['importAccount'] = request.import_account
        if not UtilClient.is_unset(request.import_demo_project):
            body['importDemoProject'] = request.import_demo_project
        if not UtilClient.is_unset(request.import_repo_type):
            body['importRepoType'] = request.import_repo_type
        if not UtilClient.is_unset(request.import_token):
            body['importToken'] = request.import_token
        if not UtilClient.is_unset(request.import_token_encrypted):
            body['importTokenEncrypted'] = request.import_token_encrypted
        if not UtilClient.is_unset(request.import_url):
            body['importUrl'] = request.import_url
        if not UtilClient.is_unset(request.init_standard_service):
            body['initStandardService'] = request.init_standard_service
        if not UtilClient.is_unset(request.is_crypto_enabled):
            body['isCryptoEnabled'] = request.is_crypto_enabled
        if not UtilClient.is_unset(request.local_import_url):
            body['localImportUrl'] = request.local_import_url
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.namespace_id):
            body['namespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.path):
            body['path'] = request.path
        if not UtilClient.is_unset(request.readme_type):
            body['readmeType'] = request.readme_type
        if not UtilClient.is_unset(request.visibility_level):
            body['visibilityLevel'] = request.visibility_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repository(
        self,
        request: devops_20210625_models.CreateRepositoryRequest,
    ) -> devops_20210625_models.CreateRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_repository_with_options(request, headers, runtime)

    async def create_repository_async(
        self,
        request: devops_20210625_models.CreateRepositoryRequest,
    ) -> devops_20210625_models.CreateRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_repository_with_options_async(request, headers, runtime)

    def create_repository_group_with_options(
        self,
        request: devops_20210625_models.CreateRepositoryGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateRepositoryGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.avatar_url):
            body['avatarUrl'] = request.avatar_url
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parent_id):
            body['parentId'] = request.parent_id
        if not UtilClient.is_unset(request.path):
            body['path'] = request.path
        if not UtilClient.is_unset(request.visibility_level):
            body['visibilityLevel'] = request.visibility_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRepositoryGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/groups/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateRepositoryGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repository_group_with_options_async(
        self,
        request: devops_20210625_models.CreateRepositoryGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateRepositoryGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.avatar_url):
            body['avatarUrl'] = request.avatar_url
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parent_id):
            body['parentId'] = request.parent_id
        if not UtilClient.is_unset(request.path):
            body['path'] = request.path
        if not UtilClient.is_unset(request.visibility_level):
            body['visibilityLevel'] = request.visibility_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRepositoryGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/groups/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateRepositoryGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repository_group(
        self,
        request: devops_20210625_models.CreateRepositoryGroupRequest,
    ) -> devops_20210625_models.CreateRepositoryGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_repository_group_with_options(request, headers, runtime)

    async def create_repository_group_async(
        self,
        request: devops_20210625_models.CreateRepositoryGroupRequest,
    ) -> devops_20210625_models.CreateRepositoryGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_repository_group_with_options_async(request, headers, runtime)

    def create_resource_member_with_options(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        request: devops_20210625_models.CreateResourceMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateResourceMemberResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(resource_type)}/{OpenApiUtilClient.get_encode_param(resource_id)}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateResourceMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_member_with_options_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        request: devops_20210625_models.CreateResourceMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateResourceMemberResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(resource_type)}/{OpenApiUtilClient.get_encode_param(resource_id)}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateResourceMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_member(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        request: devops_20210625_models.CreateResourceMemberRequest,
    ) -> devops_20210625_models.CreateResourceMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_member_with_options(organization_id, resource_type, resource_id, request, headers, runtime)

    async def create_resource_member_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        request: devops_20210625_models.CreateResourceMemberRequest,
    ) -> devops_20210625_models.CreateResourceMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_resource_member_with_options_async(organization_id, resource_type, resource_id, request, headers, runtime)

    def create_service_auth_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateServiceAuthRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateServiceAuthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_auth_type):
            query['serviceAuthType'] = request.service_auth_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceAuth',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/serviceAuths',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateServiceAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_auth_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateServiceAuthRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateServiceAuthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_auth_type):
            query['serviceAuthType'] = request.service_auth_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceAuth',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/serviceAuths',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateServiceAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_auth(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateServiceAuthRequest,
    ) -> devops_20210625_models.CreateServiceAuthResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_auth_with_options(organization_id, request, headers, runtime)

    async def create_service_auth_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateServiceAuthRequest,
    ) -> devops_20210625_models.CreateServiceAuthResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_auth_with_options_async(organization_id, request, headers, runtime)

    def create_service_connection_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateServiceConnectionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateServiceConnectionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_type):
            body['authType'] = request.auth_type
        if not UtilClient.is_unset(request.connection_name):
            body['connectionName'] = request.connection_name
        if not UtilClient.is_unset(request.connection_type):
            body['connectionType'] = request.connection_type
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.service_auth_id):
            body['serviceAuthId'] = request.service_auth_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceConnection',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/createServiceConnection',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateServiceConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_connection_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateServiceConnectionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateServiceConnectionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_type):
            body['authType'] = request.auth_type
        if not UtilClient.is_unset(request.connection_name):
            body['connectionName'] = request.connection_name
        if not UtilClient.is_unset(request.connection_type):
            body['connectionType'] = request.connection_type
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.service_auth_id):
            body['serviceAuthId'] = request.service_auth_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceConnection',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/createServiceConnection',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateServiceConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_connection(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateServiceConnectionRequest,
    ) -> devops_20210625_models.CreateServiceConnectionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_connection_with_options(organization_id, request, headers, runtime)

    async def create_service_connection_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateServiceConnectionRequest,
    ) -> devops_20210625_models.CreateServiceConnectionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_connection_with_options_async(organization_id, request, headers, runtime)

    def create_service_credential_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateServiceCredentialRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateServiceCredentialResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceCredential',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/serviceCredentials',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateServiceCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_credential_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateServiceCredentialRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateServiceCredentialResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceCredential',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/serviceCredentials',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateServiceCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_credential(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateServiceCredentialRequest,
    ) -> devops_20210625_models.CreateServiceCredentialResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_credential_with_options(organization_id, request, headers, runtime)

    async def create_service_credential_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateServiceCredentialRequest,
    ) -> devops_20210625_models.CreateServiceCredentialResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_credential_with_options_async(organization_id, request, headers, runtime)

    def create_sprint_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateSprintRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateSprintResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_date):
            body['endDate'] = request.end_date
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.space_identifier):
            body['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.staff_ids):
            body['staffIds'] = request.staff_ids
        if not UtilClient.is_unset(request.start_date):
            body['startDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSprint',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/sprints/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateSprintResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sprint_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateSprintRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateSprintResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_date):
            body['endDate'] = request.end_date
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.space_identifier):
            body['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.staff_ids):
            body['staffIds'] = request.staff_ids
        if not UtilClient.is_unset(request.start_date):
            body['startDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSprint',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/sprints/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateSprintResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sprint(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateSprintRequest,
    ) -> devops_20210625_models.CreateSprintResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_sprint_with_options(organization_id, request, headers, runtime)

    async def create_sprint_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateSprintRequest,
    ) -> devops_20210625_models.CreateSprintResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_sprint_with_options_async(organization_id, request, headers, runtime)

    def create_ssh_key_with_options(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateSshKeyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateSshKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/sshKey',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateSshKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ssh_key_with_options_async(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateSshKeyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateSshKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/sshKey',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateSshKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ssh_key(
        self,
        organization_id: str,
    ) -> devops_20210625_models.CreateSshKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ssh_key_with_options(organization_id, headers, runtime)

    async def create_ssh_key_async(
        self,
        organization_id: str,
    ) -> devops_20210625_models.CreateSshKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_ssh_key_with_options_async(organization_id, headers, runtime)

    def create_tag_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.message):
            body['message'] = request.message
        if not UtilClient.is_unset(request.ref):
            body['ref'] = request.ref
        if not UtilClient.is_unset(request.tag_name):
            body['tagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/tags/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tag_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.message):
            body['message'] = request.message
        if not UtilClient.is_unset(request.ref):
            body['ref'] = request.ref
        if not UtilClient.is_unset(request.tag_name):
            body['tagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/tags/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tag(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateTagRequest,
    ) -> devops_20210625_models.CreateTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_tag_with_options(repository_id, request, headers, runtime)

    async def create_tag_async(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateTagRequest,
    ) -> devops_20210625_models.CreateTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_tag_with_options_async(repository_id, request, headers, runtime)

    def create_test_case_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateTestCaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateTestCaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assigned_to):
            body['assignedTo'] = request.assigned_to
        if not UtilClient.is_unset(request.directory_identifier):
            body['directoryIdentifier'] = request.directory_identifier
        if not UtilClient.is_unset(request.field_value_list):
            body['fieldValueList'] = request.field_value_list
        if not UtilClient.is_unset(request.priority):
            body['priority'] = request.priority
        if not UtilClient.is_unset(request.space_identifier):
            body['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.testcase_step_content_info):
            body['testcaseStepContentInfo'] = request.testcase_step_content_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTestCase',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/testhub/testcase',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateTestCaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_test_case_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateTestCaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateTestCaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assigned_to):
            body['assignedTo'] = request.assigned_to
        if not UtilClient.is_unset(request.directory_identifier):
            body['directoryIdentifier'] = request.directory_identifier
        if not UtilClient.is_unset(request.field_value_list):
            body['fieldValueList'] = request.field_value_list
        if not UtilClient.is_unset(request.priority):
            body['priority'] = request.priority
        if not UtilClient.is_unset(request.space_identifier):
            body['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.testcase_step_content_info):
            body['testcaseStepContentInfo'] = request.testcase_step_content_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTestCase',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/testhub/testcase',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateTestCaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_test_case(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateTestCaseRequest,
    ) -> devops_20210625_models.CreateTestCaseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_test_case_with_options(organization_id, request, headers, runtime)

    async def create_test_case_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateTestCaseRequest,
    ) -> devops_20210625_models.CreateTestCaseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_test_case_with_options_async(organization_id, request, headers, runtime)

    def create_user_key_with_options(
        self,
        request: devops_20210625_models.CreateUserKeyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateUserKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.expire_time):
            body['expireTime'] = request.expire_time
        if not UtilClient.is_unset(request.key_scope):
            body['keyScope'] = request.key_scope
        if not UtilClient.is_unset(request.public_key):
            body['publicKey'] = request.public_key
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUserKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v3/user/keys/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateUserKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_key_with_options_async(
        self,
        request: devops_20210625_models.CreateUserKeyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateUserKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.expire_time):
            body['expireTime'] = request.expire_time
        if not UtilClient.is_unset(request.key_scope):
            body['keyScope'] = request.key_scope
        if not UtilClient.is_unset(request.public_key):
            body['publicKey'] = request.public_key
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUserKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v3/user/keys/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateUserKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_key(
        self,
        request: devops_20210625_models.CreateUserKeyRequest,
    ) -> devops_20210625_models.CreateUserKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_user_key_with_options(request, headers, runtime)

    async def create_user_key_async(
        self,
        request: devops_20210625_models.CreateUserKeyRequest,
    ) -> devops_20210625_models.CreateUserKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_user_key_with_options_async(request, headers, runtime)

    def create_variable_group_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateVariableGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateVariableGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/variableGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateVariableGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_variable_group_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateVariableGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateVariableGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/variableGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateVariableGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_variable_group(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateVariableGroupRequest,
    ) -> devops_20210625_models.CreateVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_variable_group_with_options(organization_id, request, headers, runtime)

    async def create_variable_group_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateVariableGroupRequest,
    ) -> devops_20210625_models.CreateVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_variable_group_with_options_async(organization_id, request, headers, runtime)

    def create_workitem_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkitemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assigned_to):
            body['assignedTo'] = request.assigned_to
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.description_format):
            body['descriptionFormat'] = request.description_format
        if not UtilClient.is_unset(request.field_value_list):
            body['fieldValueList'] = request.field_value_list
        if not UtilClient.is_unset(request.parent):
            body['parent'] = request.parent
        if not UtilClient.is_unset(request.participant):
            body['participant'] = request.participant
        if not UtilClient.is_unset(request.space):
            body['space'] = request.space
        if not UtilClient.is_unset(request.space_identifier):
            body['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            body['spaceType'] = request.space_type
        if not UtilClient.is_unset(request.sprint):
            body['sprint'] = request.sprint
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        if not UtilClient.is_unset(request.tracker):
            body['tracker'] = request.tracker
        if not UtilClient.is_unset(request.verifier):
            body['verifier'] = request.verifier
        if not UtilClient.is_unset(request.workitem_type):
            body['workitemType'] = request.workitem_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitem',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workitem_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkitemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assigned_to):
            body['assignedTo'] = request.assigned_to
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.description_format):
            body['descriptionFormat'] = request.description_format
        if not UtilClient.is_unset(request.field_value_list):
            body['fieldValueList'] = request.field_value_list
        if not UtilClient.is_unset(request.parent):
            body['parent'] = request.parent
        if not UtilClient.is_unset(request.participant):
            body['participant'] = request.participant
        if not UtilClient.is_unset(request.space):
            body['space'] = request.space
        if not UtilClient.is_unset(request.space_identifier):
            body['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            body['spaceType'] = request.space_type
        if not UtilClient.is_unset(request.sprint):
            body['sprint'] = request.sprint
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        if not UtilClient.is_unset(request.tracker):
            body['tracker'] = request.tracker
        if not UtilClient.is_unset(request.verifier):
            body['verifier'] = request.verifier
        if not UtilClient.is_unset(request.workitem_type):
            body['workitemType'] = request.workitem_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitem',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workitem(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemRequest,
    ) -> devops_20210625_models.CreateWorkitemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workitem_with_options(organization_id, request, headers, runtime)

    async def create_workitem_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemRequest,
    ) -> devops_20210625_models.CreateWorkitemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_workitem_with_options_async(organization_id, request, headers, runtime)

    def create_workitem_comment_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkitemCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.format_type):
            body['formatType'] = request.format_type
        if not UtilClient.is_unset(request.parent_id):
            body['parentId'] = request.parent_id
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitemComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/comment',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemCommentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workitem_comment_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkitemCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.format_type):
            body['formatType'] = request.format_type
        if not UtilClient.is_unset(request.parent_id):
            body['parentId'] = request.parent_id
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitemComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/comment',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemCommentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workitem_comment(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemCommentRequest,
    ) -> devops_20210625_models.CreateWorkitemCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workitem_comment_with_options(organization_id, request, headers, runtime)

    async def create_workitem_comment_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemCommentRequest,
    ) -> devops_20210625_models.CreateWorkitemCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_workitem_comment_with_options_async(organization_id, request, headers, runtime)

    def create_workitem_estimate_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemEstimateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkitemEstimateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.record_user_identifier):
            body['recordUserIdentifier'] = request.record_user_identifier
        if not UtilClient.is_unset(request.spent_time):
            body['spentTime'] = request.spent_time
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitemEstimate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/estimate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemEstimateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workitem_estimate_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemEstimateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkitemEstimateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.record_user_identifier):
            body['recordUserIdentifier'] = request.record_user_identifier
        if not UtilClient.is_unset(request.spent_time):
            body['spentTime'] = request.spent_time
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitemEstimate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/estimate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemEstimateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workitem_estimate(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemEstimateRequest,
    ) -> devops_20210625_models.CreateWorkitemEstimateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workitem_estimate_with_options(organization_id, request, headers, runtime)

    async def create_workitem_estimate_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemEstimateRequest,
    ) -> devops_20210625_models.CreateWorkitemEstimateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_workitem_estimate_with_options_async(organization_id, request, headers, runtime)

    def create_workitem_record_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemRecordRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkitemRecordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.actual_time):
            body['actualTime'] = request.actual_time
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.gmt_end):
            body['gmtEnd'] = request.gmt_end
        if not UtilClient.is_unset(request.gmt_start):
            body['gmtStart'] = request.gmt_start
        if not UtilClient.is_unset(request.record_user_identifier):
            body['recordUserIdentifier'] = request.record_user_identifier
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitemRecord',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/record',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workitem_record_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemRecordRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkitemRecordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.actual_time):
            body['actualTime'] = request.actual_time
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.gmt_end):
            body['gmtEnd'] = request.gmt_end
        if not UtilClient.is_unset(request.gmt_start):
            body['gmtStart'] = request.gmt_start
        if not UtilClient.is_unset(request.record_user_identifier):
            body['recordUserIdentifier'] = request.record_user_identifier
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitemRecord',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/record',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workitem_record(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemRecordRequest,
    ) -> devops_20210625_models.CreateWorkitemRecordResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workitem_record_with_options(organization_id, request, headers, runtime)

    async def create_workitem_record_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemRecordRequest,
    ) -> devops_20210625_models.CreateWorkitemRecordResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_workitem_record_with_options_async(organization_id, request, headers, runtime)

    def create_workitem_v2with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkitemV2Response:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assigned_to):
            body['assignedTo'] = request.assigned_to
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.field_value_list):
            body['fieldValueList'] = request.field_value_list
        if not UtilClient.is_unset(request.parent_identifier):
            body['parentIdentifier'] = request.parent_identifier
        if not UtilClient.is_unset(request.participants):
            body['participants'] = request.participants
        if not UtilClient.is_unset(request.space_identifier):
            body['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.sprint_identifier):
            body['sprintIdentifier'] = request.sprint_identifier
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.trackers):
            body['trackers'] = request.trackers
        if not UtilClient.is_unset(request.verifier):
            body['verifier'] = request.verifier
        if not UtilClient.is_unset(request.versions):
            body['versions'] = request.versions
        if not UtilClient.is_unset(request.workitem_type_identifier):
            body['workitemTypeIdentifier'] = request.workitem_type_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitemV2',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemV2Response(),
            self.call_api(params, req, runtime)
        )

    async def create_workitem_v2with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkitemV2Response:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assigned_to):
            body['assignedTo'] = request.assigned_to
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.field_value_list):
            body['fieldValueList'] = request.field_value_list
        if not UtilClient.is_unset(request.parent_identifier):
            body['parentIdentifier'] = request.parent_identifier
        if not UtilClient.is_unset(request.participants):
            body['participants'] = request.participants
        if not UtilClient.is_unset(request.space_identifier):
            body['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.sprint_identifier):
            body['sprintIdentifier'] = request.sprint_identifier
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.trackers):
            body['trackers'] = request.trackers
        if not UtilClient.is_unset(request.verifier):
            body['verifier'] = request.verifier
        if not UtilClient.is_unset(request.versions):
            body['versions'] = request.versions
        if not UtilClient.is_unset(request.workitem_type_identifier):
            body['workitemTypeIdentifier'] = request.workitem_type_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitemV2',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workitem_v2(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemV2Request,
    ) -> devops_20210625_models.CreateWorkitemV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workitem_v2with_options(organization_id, request, headers, runtime)

    async def create_workitem_v2_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemV2Request,
    ) -> devops_20210625_models.CreateWorkitemV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_workitem_v2with_options_async(organization_id, request, headers, runtime)

    def create_workspace_with_options(
        self,
        request: devops_20210625_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkspaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_url):
            body['codeUrl'] = request.code_url
        if not UtilClient.is_unset(request.code_version):
            body['codeVersion'] = request.code_version
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.request_from):
            body['requestFrom'] = request.request_from
        if not UtilClient.is_unset(request.resource_identifier):
            body['resourceIdentifier'] = request.resource_identifier
        if not UtilClient.is_unset(request.reuse):
            body['reuse'] = request.reuse
        if not UtilClient.is_unset(request.workspace_template):
            body['workspaceTemplate'] = request.workspace_template
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workspace_with_options_async(
        self,
        request: devops_20210625_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkspaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_url):
            body['codeUrl'] = request.code_url
        if not UtilClient.is_unset(request.code_version):
            body['codeVersion'] = request.code_version
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.request_from):
            body['requestFrom'] = request.request_from
        if not UtilClient.is_unset(request.resource_identifier):
            body['resourceIdentifier'] = request.resource_identifier
        if not UtilClient.is_unset(request.reuse):
            body['reuse'] = request.reuse
        if not UtilClient.is_unset(request.workspace_template):
            body['workspaceTemplate'] = request.workspace_template
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workspace(
        self,
        request: devops_20210625_models.CreateWorkspaceRequest,
    ) -> devops_20210625_models.CreateWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workspace_with_options(request, headers, runtime)

    async def create_workspace_async(
        self,
        request: devops_20210625_models.CreateWorkspaceRequest,
    ) -> devops_20210625_models.CreateWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_workspace_with_options_async(request, headers, runtime)

    def delete_app_member_with_options(
        self,
        app_name: str,
        request: devops_20210625_models.DeleteAppMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteAppMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.subject_id):
            query['subjectId'] = request.subject_id
        if not UtilClient.is_unset(request.subject_type):
            query['subjectType'] = request.subject_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/appstack/apps/{OpenApiUtilClient.get_encode_param(app_name)}/members',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteAppMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_member_with_options_async(
        self,
        app_name: str,
        request: devops_20210625_models.DeleteAppMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteAppMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.subject_id):
            query['subjectId'] = request.subject_id
        if not UtilClient.is_unset(request.subject_type):
            query['subjectType'] = request.subject_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/appstack/apps/{OpenApiUtilClient.get_encode_param(app_name)}/members',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteAppMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_member(
        self,
        app_name: str,
        request: devops_20210625_models.DeleteAppMemberRequest,
    ) -> devops_20210625_models.DeleteAppMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_app_member_with_options(app_name, request, headers, runtime)

    async def delete_app_member_async(
        self,
        app_name: str,
        request: devops_20210625_models.DeleteAppMemberRequest,
    ) -> devops_20210625_models.DeleteAppMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_app_member_with_options_async(app_name, request, headers, runtime)

    def delete_branch_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.branch_name):
            query['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBranch',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/branches/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteBranchResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_branch_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.branch_name):
            query['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBranch',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/branches/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteBranchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_branch(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteBranchRequest,
    ) -> devops_20210625_models.DeleteBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_branch_with_options(repository_id, request, headers, runtime)

    async def delete_branch_async(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteBranchRequest,
    ) -> devops_20210625_models.DeleteBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_branch_with_options_async(repository_id, request, headers, runtime)

    def delete_file_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.branch_name):
            query['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.commit_message):
            query['commitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_file_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.branch_name):
            query['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.commit_message):
            query['commitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_file(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteFileRequest,
    ) -> devops_20210625_models.DeleteFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_file_with_options(repository_id, request, headers, runtime)

    async def delete_file_async(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteFileRequest,
    ) -> devops_20210625_models.DeleteFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_file_with_options_async(repository_id, request, headers, runtime)

    def delete_flow_tag_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteFlowTagResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tags/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteFlowTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_tag_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteFlowTagResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tags/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteFlowTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow_tag(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteFlowTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_flow_tag_with_options(organization_id, id, headers, runtime)

    async def delete_flow_tag_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteFlowTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_flow_tag_with_options_async(organization_id, id, headers, runtime)

    def delete_flow_tag_group_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteFlowTagGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tagGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteFlowTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_tag_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteFlowTagGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tagGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteFlowTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow_tag_group(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_flow_tag_group_with_options(organization_id, id, headers, runtime)

    async def delete_flow_tag_group_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_flow_tag_group_with_options_async(organization_id, id, headers, runtime)

    def delete_group_member_with_options(
        self,
        group_id: str,
        request: devops_20210625_models.DeleteGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.aliyun_pk):
            query['aliyunPk'] = request.aliyun_pk
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.member_type):
            body['memberType'] = request.member_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGroupMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/groups/{OpenApiUtilClient.get_encode_param(group_id)}/members/remove/aliyun_pk',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_member_with_options_async(
        self,
        group_id: str,
        request: devops_20210625_models.DeleteGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.aliyun_pk):
            query['aliyunPk'] = request.aliyun_pk
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.member_type):
            body['memberType'] = request.member_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGroupMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/groups/{OpenApiUtilClient.get_encode_param(group_id)}/members/remove/aliyun_pk',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group_member(
        self,
        group_id: str,
        request: devops_20210625_models.DeleteGroupMemberRequest,
    ) -> devops_20210625_models.DeleteGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_group_member_with_options(group_id, request, headers, runtime)

    async def delete_group_member_async(
        self,
        group_id: str,
        request: devops_20210625_models.DeleteGroupMemberRequest,
    ) -> devops_20210625_models.DeleteGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_group_member_with_options_async(group_id, request, headers, runtime)

    def delete_host_group_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteHostGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/hostGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_host_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteHostGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/hostGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_host_group(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_host_group_with_options(organization_id, id, headers, runtime)

    async def delete_host_group_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_host_group_with_options_async(organization_id, id, headers, runtime)

    def delete_pipeline_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeletePipelineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeletePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pipeline_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeletePipelineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeletePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pipeline(
        self,
        organization_id: str,
        pipeline_id: str,
    ) -> devops_20210625_models.DeletePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipeline_with_options(organization_id, pipeline_id, headers, runtime)

    async def delete_pipeline_async(
        self,
        organization_id: str,
        pipeline_id: str,
    ) -> devops_20210625_models.DeletePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_pipeline_with_options_async(organization_id, pipeline_id, headers, runtime)

    def delete_pipeline_group_with_options(
        self,
        organization_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeletePipelineGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeletePipelineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pipeline_group_with_options_async(
        self,
        organization_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeletePipelineGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeletePipelineGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pipeline_group(
        self,
        organization_id: str,
        group_id: str,
    ) -> devops_20210625_models.DeletePipelineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipeline_group_with_options(organization_id, group_id, headers, runtime)

    async def delete_pipeline_group_async(
        self,
        organization_id: str,
        group_id: str,
    ) -> devops_20210625_models.DeletePipelineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_pipeline_group_with_options_async(organization_id, group_id, headers, runtime)

    def delete_pipeline_relations_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.DeletePipelineRelationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeletePipelineRelationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rel_object_id):
            query['relObjectId'] = request.rel_object_id
        if not UtilClient.is_unset(request.rel_object_type):
            query['relObjectType'] = request.rel_object_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePipelineRelations',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRelations',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeletePipelineRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pipeline_relations_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.DeletePipelineRelationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeletePipelineRelationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rel_object_id):
            query['relObjectId'] = request.rel_object_id
        if not UtilClient.is_unset(request.rel_object_type):
            query['relObjectType'] = request.rel_object_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePipelineRelations',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRelations',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeletePipelineRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pipeline_relations(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.DeletePipelineRelationsRequest,
    ) -> devops_20210625_models.DeletePipelineRelationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipeline_relations_with_options(organization_id, pipeline_id, request, headers, runtime)

    async def delete_pipeline_relations_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.DeletePipelineRelationsRequest,
    ) -> devops_20210625_models.DeletePipelineRelationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_pipeline_relations_with_options_async(organization_id, pipeline_id, request, headers, runtime)

    def delete_project_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteProjectRequest,
    ) -> devops_20210625_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(organization_id, request, headers, runtime)

    async def delete_project_async(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteProjectRequest,
    ) -> devops_20210625_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_project_with_options_async(organization_id, request, headers, runtime)

    def delete_project_label_with_options(
        self,
        label_id: str,
        request: devops_20210625_models.DeleteProjectLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteProjectLabelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProjectLabel',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/labels/{OpenApiUtilClient.get_encode_param(label_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteProjectLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_label_with_options_async(
        self,
        label_id: str,
        request: devops_20210625_models.DeleteProjectLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteProjectLabelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProjectLabel',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/labels/{OpenApiUtilClient.get_encode_param(label_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteProjectLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project_label(
        self,
        label_id: str,
        request: devops_20210625_models.DeleteProjectLabelRequest,
    ) -> devops_20210625_models.DeleteProjectLabelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_label_with_options(label_id, request, headers, runtime)

    async def delete_project_label_async(
        self,
        label_id: str,
        request: devops_20210625_models.DeleteProjectLabelRequest,
    ) -> devops_20210625_models.DeleteProjectLabelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_project_label_with_options_async(label_id, request, headers, runtime)

    def delete_protected_branch_with_options(
        self,
        repository_id: str,
        protected_branch_id: str,
        request: devops_20210625_models.DeleteProtectedBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteProtectedBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProtectedBranch',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/protect_branches/{OpenApiUtilClient.get_encode_param(protected_branch_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteProtectedBranchResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_protected_branch_with_options_async(
        self,
        repository_id: str,
        protected_branch_id: str,
        request: devops_20210625_models.DeleteProtectedBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteProtectedBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProtectedBranch',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/protect_branches/{OpenApiUtilClient.get_encode_param(protected_branch_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteProtectedBranchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_protected_branch(
        self,
        repository_id: str,
        protected_branch_id: str,
        request: devops_20210625_models.DeleteProtectedBranchRequest,
    ) -> devops_20210625_models.DeleteProtectedBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_protected_branch_with_options(repository_id, protected_branch_id, request, headers, runtime)

    async def delete_protected_branch_async(
        self,
        repository_id: str,
        protected_branch_id: str,
        request: devops_20210625_models.DeleteProtectedBranchRequest,
    ) -> devops_20210625_models.DeleteProtectedBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_protected_branch_with_options_async(repository_id, protected_branch_id, request, headers, runtime)

    def delete_push_rule_with_options(
        self,
        repository_id: str,
        push_rule_id: str,
        request: devops_20210625_models.DeletePushRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeletePushRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePushRule',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/push_rule/{OpenApiUtilClient.get_encode_param(push_rule_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeletePushRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_push_rule_with_options_async(
        self,
        repository_id: str,
        push_rule_id: str,
        request: devops_20210625_models.DeletePushRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeletePushRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePushRule',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/push_rule/{OpenApiUtilClient.get_encode_param(push_rule_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeletePushRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_push_rule(
        self,
        repository_id: str,
        push_rule_id: str,
        request: devops_20210625_models.DeletePushRuleRequest,
    ) -> devops_20210625_models.DeletePushRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_push_rule_with_options(repository_id, push_rule_id, request, headers, runtime)

    async def delete_push_rule_async(
        self,
        repository_id: str,
        push_rule_id: str,
        request: devops_20210625_models.DeletePushRuleRequest,
    ) -> devops_20210625_models.DeletePushRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_push_rule_with_options_async(repository_id, push_rule_id, request, headers, runtime)

    def delete_repository_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.reason):
            body['reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/remove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repository_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.reason):
            body['reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/remove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_repository(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteRepositoryRequest,
    ) -> devops_20210625_models.DeleteRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_with_options(repository_id, request, headers, runtime)

    async def delete_repository_async(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteRepositoryRequest,
    ) -> devops_20210625_models.DeleteRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_repository_with_options_async(repository_id, request, headers, runtime)

    def delete_repository_group_with_options(
        self,
        group_id: str,
        request: devops_20210625_models.DeleteRepositoryGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteRepositoryGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.reason):
            body['reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRepositoryGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/groups/{OpenApiUtilClient.get_encode_param(group_id)}/remove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteRepositoryGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repository_group_with_options_async(
        self,
        group_id: str,
        request: devops_20210625_models.DeleteRepositoryGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteRepositoryGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.reason):
            body['reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRepositoryGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/groups/{OpenApiUtilClient.get_encode_param(group_id)}/remove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteRepositoryGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_repository_group(
        self,
        group_id: str,
        request: devops_20210625_models.DeleteRepositoryGroupRequest,
    ) -> devops_20210625_models.DeleteRepositoryGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_group_with_options(group_id, request, headers, runtime)

    async def delete_repository_group_async(
        self,
        group_id: str,
        request: devops_20210625_models.DeleteRepositoryGroupRequest,
    ) -> devops_20210625_models.DeleteRepositoryGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_repository_group_with_options_async(group_id, request, headers, runtime)

    def delete_repository_member_with_options(
        self,
        repository_id: str,
        aliyun_pk: str,
        request: devops_20210625_models.DeleteRepositoryMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteRepositoryMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.member_type):
            body['memberType'] = request.member_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRepositoryMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/members/delete/{OpenApiUtilClient.get_encode_param(aliyun_pk)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteRepositoryMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repository_member_with_options_async(
        self,
        repository_id: str,
        aliyun_pk: str,
        request: devops_20210625_models.DeleteRepositoryMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteRepositoryMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.member_type):
            body['memberType'] = request.member_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRepositoryMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/members/delete/{OpenApiUtilClient.get_encode_param(aliyun_pk)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteRepositoryMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_repository_member(
        self,
        repository_id: str,
        aliyun_pk: str,
        request: devops_20210625_models.DeleteRepositoryMemberRequest,
    ) -> devops_20210625_models.DeleteRepositoryMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_member_with_options(repository_id, aliyun_pk, request, headers, runtime)

    async def delete_repository_member_async(
        self,
        repository_id: str,
        aliyun_pk: str,
        request: devops_20210625_models.DeleteRepositoryMemberRequest,
    ) -> devops_20210625_models.DeleteRepositoryMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_repository_member_with_options_async(repository_id, aliyun_pk, request, headers, runtime)

    def delete_repository_webhook_with_options(
        self,
        repository_id: str,
        hook_id: str,
        request: devops_20210625_models.DeleteRepositoryWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteRepositoryWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepositoryWebhook',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/hooks/{OpenApiUtilClient.get_encode_param(hook_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteRepositoryWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repository_webhook_with_options_async(
        self,
        repository_id: str,
        hook_id: str,
        request: devops_20210625_models.DeleteRepositoryWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteRepositoryWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepositoryWebhook',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/hooks/{OpenApiUtilClient.get_encode_param(hook_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteRepositoryWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_repository_webhook(
        self,
        repository_id: str,
        hook_id: str,
        request: devops_20210625_models.DeleteRepositoryWebhookRequest,
    ) -> devops_20210625_models.DeleteRepositoryWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_webhook_with_options(repository_id, hook_id, request, headers, runtime)

    async def delete_repository_webhook_async(
        self,
        repository_id: str,
        hook_id: str,
        request: devops_20210625_models.DeleteRepositoryWebhookRequest,
    ) -> devops_20210625_models.DeleteRepositoryWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_repository_webhook_with_options_async(repository_id, hook_id, request, headers, runtime)

    def delete_resource_member_with_options(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteResourceMemberResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(resource_type)}/{OpenApiUtilClient.get_encode_param(resource_id)}/members/{OpenApiUtilClient.get_encode_param(account_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteResourceMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_member_with_options_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteResourceMemberResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(resource_type)}/{OpenApiUtilClient.get_encode_param(resource_id)}/members/{OpenApiUtilClient.get_encode_param(account_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteResourceMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_member(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
    ) -> devops_20210625_models.DeleteResourceMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_member_with_options(organization_id, resource_type, resource_id, account_id, headers, runtime)

    async def delete_resource_member_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
    ) -> devops_20210625_models.DeleteResourceMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_member_with_options_async(organization_id, resource_type, resource_id, account_id, headers, runtime)

    def delete_tag_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.tag_name):
            query['tagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/tags/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tag_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.tag_name):
            query['tagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/tags/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tag(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteTagRequest,
    ) -> devops_20210625_models.DeleteTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_tag_with_options(repository_id, request, headers, runtime)

    async def delete_tag_async(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteTagRequest,
    ) -> devops_20210625_models.DeleteTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_tag_with_options_async(repository_id, request, headers, runtime)

    def delete_user_key_with_options(
        self,
        key_id: str,
        request: devops_20210625_models.DeleteUserKeyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteUserKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v3/user/keys/{OpenApiUtilClient.get_encode_param(key_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteUserKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_key_with_options_async(
        self,
        key_id: str,
        request: devops_20210625_models.DeleteUserKeyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteUserKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v3/user/keys/{OpenApiUtilClient.get_encode_param(key_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteUserKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_key(
        self,
        key_id: str,
        request: devops_20210625_models.DeleteUserKeyRequest,
    ) -> devops_20210625_models.DeleteUserKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_user_key_with_options(key_id, request, headers, runtime)

    async def delete_user_key_async(
        self,
        key_id: str,
        request: devops_20210625_models.DeleteUserKeyRequest,
    ) -> devops_20210625_models.DeleteUserKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_user_key_with_options_async(key_id, request, headers, runtime)

    def delete_variable_group_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteVariableGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/variableGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteVariableGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_variable_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteVariableGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/variableGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteVariableGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_variable_group(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_variable_group_with_options(organization_id, id, headers, runtime)

    async def delete_variable_group_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_variable_group_with_options_async(organization_id, id, headers, runtime)

    def delete_workitem_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteWorkitemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteWorkitemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkitem',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitem/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteWorkitemResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workitem_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteWorkitemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteWorkitemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkitem',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitem/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteWorkitemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workitem(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteWorkitemRequest,
    ) -> devops_20210625_models.DeleteWorkitemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_workitem_with_options(organization_id, request, headers, runtime)

    async def delete_workitem_async(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteWorkitemRequest,
    ) -> devops_20210625_models.DeleteWorkitemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_workitem_with_options_async(organization_id, request, headers, runtime)

    def delete_workitem_all_comment_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteWorkitemAllCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteWorkitemAllCommentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkitemAllComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/deleteAllComment',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteWorkitemAllCommentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workitem_all_comment_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteWorkitemAllCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteWorkitemAllCommentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkitemAllComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/deleteAllComment',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteWorkitemAllCommentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workitem_all_comment(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteWorkitemAllCommentRequest,
    ) -> devops_20210625_models.DeleteWorkitemAllCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_workitem_all_comment_with_options(organization_id, request, headers, runtime)

    async def delete_workitem_all_comment_async(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteWorkitemAllCommentRequest,
    ) -> devops_20210625_models.DeleteWorkitemAllCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_workitem_all_comment_with_options_async(organization_id, request, headers, runtime)

    def delete_workitem_comment_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteWorkitemCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteWorkitemCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment_id):
            body['commentId'] = request.comment_id
        if not UtilClient.is_unset(request.identifier):
            body['identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWorkitemComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/deleteComent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteWorkitemCommentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workitem_comment_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteWorkitemCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteWorkitemCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment_id):
            body['commentId'] = request.comment_id
        if not UtilClient.is_unset(request.identifier):
            body['identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWorkitemComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/deleteComent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteWorkitemCommentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workitem_comment(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteWorkitemCommentRequest,
    ) -> devops_20210625_models.DeleteWorkitemCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_workitem_comment_with_options(organization_id, request, headers, runtime)

    async def delete_workitem_comment_async(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteWorkitemCommentRequest,
    ) -> devops_20210625_models.DeleteWorkitemCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_workitem_comment_with_options_async(organization_id, request, headers, runtime)

    def enable_deploy_key_with_options(
        self,
        repository_id: str,
        key_id: str,
        request: devops_20210625_models.EnableDeployKeyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.EnableDeployKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDeployKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/keys/{OpenApiUtilClient.get_encode_param(key_id)}/enable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.EnableDeployKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_deploy_key_with_options_async(
        self,
        repository_id: str,
        key_id: str,
        request: devops_20210625_models.EnableDeployKeyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.EnableDeployKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDeployKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/keys/{OpenApiUtilClient.get_encode_param(key_id)}/enable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.EnableDeployKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_deploy_key(
        self,
        repository_id: str,
        key_id: str,
        request: devops_20210625_models.EnableDeployKeyRequest,
    ) -> devops_20210625_models.EnableDeployKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_deploy_key_with_options(repository_id, key_id, request, headers, runtime)

    async def enable_deploy_key_async(
        self,
        repository_id: str,
        key_id: str,
        request: devops_20210625_models.EnableDeployKeyRequest,
    ) -> devops_20210625_models.EnableDeployKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.enable_deploy_key_with_options_async(repository_id, key_id, request, headers, runtime)

    def frozen_workspace_with_options(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.FrozenWorkspaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='FrozenWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/frozen',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.FrozenWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def frozen_workspace_with_options_async(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.FrozenWorkspaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='FrozenWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/frozen',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.FrozenWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def frozen_workspace(
        self,
        workspace_id: str,
    ) -> devops_20210625_models.FrozenWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.frozen_workspace_with_options(workspace_id, headers, runtime)

    async def frozen_workspace_async(
        self,
        workspace_id: str,
    ) -> devops_20210625_models.FrozenWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.frozen_workspace_with_options_async(workspace_id, headers, runtime)

    def get_application_with_options(
        self,
        app_name: str,
        request: devops_20210625_models.GetApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/appstack/apps/{OpenApiUtilClient.get_encode_param(app_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_with_options_async(
        self,
        app_name: str,
        request: devops_20210625_models.GetApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/appstack/apps/{OpenApiUtilClient.get_encode_param(app_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application(
        self,
        app_name: str,
        request: devops_20210625_models.GetApplicationRequest,
    ) -> devops_20210625_models.GetApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_application_with_options(app_name, request, headers, runtime)

    async def get_application_async(
        self,
        app_name: str,
        request: devops_20210625_models.GetApplicationRequest,
    ) -> devops_20210625_models.GetApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_application_with_options_async(app_name, request, headers, runtime)

    def get_branch_info_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.GetBranchInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetBranchInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.branch_name):
            query['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBranchInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/branches/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetBranchInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_branch_info_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.GetBranchInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetBranchInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.branch_name):
            query['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBranchInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/branches/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetBranchInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_branch_info(
        self,
        repository_id: str,
        request: devops_20210625_models.GetBranchInfoRequest,
    ) -> devops_20210625_models.GetBranchInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_branch_info_with_options(repository_id, request, headers, runtime)

    async def get_branch_info_async(
        self,
        repository_id: str,
        request: devops_20210625_models.GetBranchInfoRequest,
    ) -> devops_20210625_models.GetBranchInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_branch_info_with_options_async(repository_id, request, headers, runtime)

    def get_check_run_with_options(
        self,
        request: devops_20210625_models.GetCheckRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetCheckRunResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.check_run_id):
            query['checkRunId'] = request.check_run_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCheckRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/check_runs/get_check_run',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetCheckRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_check_run_with_options_async(
        self,
        request: devops_20210625_models.GetCheckRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetCheckRunResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.check_run_id):
            query['checkRunId'] = request.check_run_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCheckRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/check_runs/get_check_run',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetCheckRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_check_run(
        self,
        request: devops_20210625_models.GetCheckRunRequest,
    ) -> devops_20210625_models.GetCheckRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_check_run_with_options(request, headers, runtime)

    async def get_check_run_async(
        self,
        request: devops_20210625_models.GetCheckRunRequest,
    ) -> devops_20210625_models.GetCheckRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_check_run_with_options_async(request, headers, runtime)

    def get_codeup_organization_with_options(
        self,
        identity: str,
        request: devops_20210625_models.GetCodeupOrganizationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetCodeupOrganizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCodeupOrganization',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/organization/{OpenApiUtilClient.get_encode_param(identity)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetCodeupOrganizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_codeup_organization_with_options_async(
        self,
        identity: str,
        request: devops_20210625_models.GetCodeupOrganizationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetCodeupOrganizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCodeupOrganization',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/organization/{OpenApiUtilClient.get_encode_param(identity)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetCodeupOrganizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_codeup_organization(
        self,
        identity: str,
        request: devops_20210625_models.GetCodeupOrganizationRequest,
    ) -> devops_20210625_models.GetCodeupOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_codeup_organization_with_options(identity, request, headers, runtime)

    async def get_codeup_organization_async(
        self,
        identity: str,
        request: devops_20210625_models.GetCodeupOrganizationRequest,
    ) -> devops_20210625_models.GetCodeupOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_codeup_organization_with_options_async(identity, request, headers, runtime)

    def get_compare_detail_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.GetCompareDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetCompareDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.max_diff_byte):
            query['maxDiffByte'] = request.max_diff_byte
        if not UtilClient.is_unset(request.max_diff_file):
            query['maxDiffFile'] = request.max_diff_file
        if not UtilClient.is_unset(request.merge_base):
            query['mergeBase'] = request.merge_base
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCompareDetail',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/commits/compare/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetCompareDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_compare_detail_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.GetCompareDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetCompareDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.max_diff_byte):
            query['maxDiffByte'] = request.max_diff_byte
        if not UtilClient.is_unset(request.max_diff_file):
            query['maxDiffFile'] = request.max_diff_file
        if not UtilClient.is_unset(request.merge_base):
            query['mergeBase'] = request.merge_base
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCompareDetail',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/commits/compare/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetCompareDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_compare_detail(
        self,
        repository_id: str,
        request: devops_20210625_models.GetCompareDetailRequest,
    ) -> devops_20210625_models.GetCompareDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_compare_detail_with_options(repository_id, request, headers, runtime)

    async def get_compare_detail_async(
        self,
        repository_id: str,
        request: devops_20210625_models.GetCompareDetailRequest,
    ) -> devops_20210625_models.GetCompareDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_compare_detail_with_options_async(repository_id, request, headers, runtime)

    def get_custom_field_option_with_options(
        self,
        organization_id: str,
        field_id: str,
        request: devops_20210625_models.GetCustomFieldOptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetCustomFieldOptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        if not UtilClient.is_unset(request.workitem_type_identifier):
            query['workitemTypeIdentifier'] = request.workitem_type_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomFieldOption',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/fields/{OpenApiUtilClient.get_encode_param(field_id)}/getCustomOption',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetCustomFieldOptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_field_option_with_options_async(
        self,
        organization_id: str,
        field_id: str,
        request: devops_20210625_models.GetCustomFieldOptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetCustomFieldOptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        if not UtilClient.is_unset(request.workitem_type_identifier):
            query['workitemTypeIdentifier'] = request.workitem_type_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomFieldOption',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/fields/{OpenApiUtilClient.get_encode_param(field_id)}/getCustomOption',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetCustomFieldOptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_field_option(
        self,
        organization_id: str,
        field_id: str,
        request: devops_20210625_models.GetCustomFieldOptionRequest,
    ) -> devops_20210625_models.GetCustomFieldOptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_custom_field_option_with_options(organization_id, field_id, request, headers, runtime)

    async def get_custom_field_option_async(
        self,
        organization_id: str,
        field_id: str,
        request: devops_20210625_models.GetCustomFieldOptionRequest,
    ) -> devops_20210625_models.GetCustomFieldOptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_custom_field_option_with_options_async(organization_id, field_id, request, headers, runtime)

    def get_file_blobs_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.GetFileBlobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetFileBlobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.ref):
            query['ref'] = request.ref
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileBlobs',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files/blobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetFileBlobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_blobs_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.GetFileBlobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetFileBlobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.ref):
            query['ref'] = request.ref
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileBlobs',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files/blobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetFileBlobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_blobs(
        self,
        repository_id: str,
        request: devops_20210625_models.GetFileBlobsRequest,
    ) -> devops_20210625_models.GetFileBlobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_file_blobs_with_options(repository_id, request, headers, runtime)

    async def get_file_blobs_async(
        self,
        repository_id: str,
        request: devops_20210625_models.GetFileBlobsRequest,
    ) -> devops_20210625_models.GetFileBlobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_file_blobs_with_options_async(repository_id, request, headers, runtime)

    def get_file_last_commit_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.GetFileLastCommitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetFileLastCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sha):
            query['sha'] = request.sha
        if not UtilClient.is_unset(request.show_signature):
            query['showSignature'] = request.show_signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileLastCommit',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files/lastCommit',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetFileLastCommitResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_last_commit_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.GetFileLastCommitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetFileLastCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sha):
            query['sha'] = request.sha
        if not UtilClient.is_unset(request.show_signature):
            query['showSignature'] = request.show_signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileLastCommit',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files/lastCommit',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetFileLastCommitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_last_commit(
        self,
        repository_id: str,
        request: devops_20210625_models.GetFileLastCommitRequest,
    ) -> devops_20210625_models.GetFileLastCommitResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_file_last_commit_with_options(repository_id, request, headers, runtime)

    async def get_file_last_commit_async(
        self,
        repository_id: str,
        request: devops_20210625_models.GetFileLastCommitRequest,
    ) -> devops_20210625_models.GetFileLastCommitResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_file_last_commit_with_options_async(repository_id, request, headers, runtime)

    def get_flow_tag_group_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetFlowTagGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tagGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetFlowTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_flow_tag_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetFlowTagGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tagGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetFlowTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_flow_tag_group(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.GetFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_flow_tag_group_with_options(organization_id, id, headers, runtime)

    async def get_flow_tag_group_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.GetFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_flow_tag_group_with_options_async(organization_id, id, headers, runtime)

    def get_group_by_path_with_options(
        self,
        request: devops_20210625_models.GetGroupByPathRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetGroupByPathResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity):
            query['identity'] = request.identity
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroupByPath',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/4/groups/find_by_path',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetGroupByPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_group_by_path_with_options_async(
        self,
        request: devops_20210625_models.GetGroupByPathRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetGroupByPathResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity):
            query['identity'] = request.identity
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroupByPath',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/4/groups/find_by_path',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetGroupByPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_group_by_path(
        self,
        request: devops_20210625_models.GetGroupByPathRequest,
    ) -> devops_20210625_models.GetGroupByPathResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_group_by_path_with_options(request, headers, runtime)

    async def get_group_by_path_async(
        self,
        request: devops_20210625_models.GetGroupByPathRequest,
    ) -> devops_20210625_models.GetGroupByPathResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_group_by_path_with_options_async(request, headers, runtime)

    def get_group_detail_with_options(
        self,
        request: devops_20210625_models.GetGroupDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroupDetail',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/groups/get_detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_group_detail_with_options_async(
        self,
        request: devops_20210625_models.GetGroupDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroupDetail',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/groups/get_detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetGroupDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_group_detail(
        self,
        request: devops_20210625_models.GetGroupDetailRequest,
    ) -> devops_20210625_models.GetGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_group_detail_with_options(request, headers, runtime)

    async def get_group_detail_async(
        self,
        request: devops_20210625_models.GetGroupDetailRequest,
    ) -> devops_20210625_models.GetGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_group_detail_with_options_async(request, headers, runtime)

    def get_host_group_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetHostGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/hostGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_host_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetHostGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/hostGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_host_group(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.GetHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_host_group_with_options(organization_id, id, headers, runtime)

    async def get_host_group_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.GetHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_host_group_with_options_async(organization_id, id, headers, runtime)

    def get_merge_request_with_options(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.GetMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMergeRequest',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/merge_requests/{OpenApiUtilClient.get_encode_param(local_id)}/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetMergeRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_merge_request_with_options_async(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.GetMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMergeRequest',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/merge_requests/{OpenApiUtilClient.get_encode_param(local_id)}/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetMergeRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_merge_request(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.GetMergeRequestRequest,
    ) -> devops_20210625_models.GetMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_merge_request_with_options(repository_id, local_id, request, headers, runtime)

    async def get_merge_request_async(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.GetMergeRequestRequest,
    ) -> devops_20210625_models.GetMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_merge_request_with_options_async(repository_id, local_id, request, headers, runtime)

    def get_merge_request_change_tree_with_options(
        self,
        request: devops_20210625_models.GetMergeRequestChangeTreeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetMergeRequestChangeTreeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.from_patch_set_biz_id):
            query['fromPatchSetBizId'] = request.from_patch_set_biz_id
        if not UtilClient.is_unset(request.local_id):
            query['localId'] = request.local_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        if not UtilClient.is_unset(request.to_patch_set_biz_id):
            query['toPatchSetBizId'] = request.to_patch_set_biz_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMergeRequestChangeTree',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/merge_requests/diffs/change_tree',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetMergeRequestChangeTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_merge_request_change_tree_with_options_async(
        self,
        request: devops_20210625_models.GetMergeRequestChangeTreeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetMergeRequestChangeTreeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.from_patch_set_biz_id):
            query['fromPatchSetBizId'] = request.from_patch_set_biz_id
        if not UtilClient.is_unset(request.local_id):
            query['localId'] = request.local_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        if not UtilClient.is_unset(request.to_patch_set_biz_id):
            query['toPatchSetBizId'] = request.to_patch_set_biz_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMergeRequestChangeTree',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/merge_requests/diffs/change_tree',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetMergeRequestChangeTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_merge_request_change_tree(
        self,
        request: devops_20210625_models.GetMergeRequestChangeTreeRequest,
    ) -> devops_20210625_models.GetMergeRequestChangeTreeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_merge_request_change_tree_with_options(request, headers, runtime)

    async def get_merge_request_change_tree_async(
        self,
        request: devops_20210625_models.GetMergeRequestChangeTreeRequest,
    ) -> devops_20210625_models.GetMergeRequestChangeTreeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_merge_request_change_tree_with_options_async(request, headers, runtime)

    def get_organization_member_with_options(
        self,
        organization_id: str,
        account_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetOrganizationMemberResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOrganizationMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/members/{OpenApiUtilClient.get_encode_param(account_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetOrganizationMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_organization_member_with_options_async(
        self,
        organization_id: str,
        account_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetOrganizationMemberResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOrganizationMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/members/{OpenApiUtilClient.get_encode_param(account_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetOrganizationMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_organization_member(
        self,
        organization_id: str,
        account_id: str,
    ) -> devops_20210625_models.GetOrganizationMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_organization_member_with_options(organization_id, account_id, headers, runtime)

    async def get_organization_member_async(
        self,
        organization_id: str,
        account_id: str,
    ) -> devops_20210625_models.GetOrganizationMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_organization_member_with_options_async(organization_id, account_id, headers, runtime)

    def get_pipeline_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline(
        self,
        organization_id: str,
        pipeline_id: str,
    ) -> devops_20210625_models.GetPipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_with_options(organization_id, pipeline_id, headers, runtime)

    async def get_pipeline_async(
        self,
        organization_id: str,
        pipeline_id: str,
    ) -> devops_20210625_models.GetPipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_with_options_async(organization_id, pipeline_id, headers, runtime)

    def get_pipeline_artifact_url_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.GetPipelineArtifactUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineArtifactUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPipelineArtifactUrl',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/getArtifactDownloadUrl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineArtifactUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_artifact_url_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.GetPipelineArtifactUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineArtifactUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPipelineArtifactUrl',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/getArtifactDownloadUrl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineArtifactUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_artifact_url(
        self,
        organization_id: str,
        request: devops_20210625_models.GetPipelineArtifactUrlRequest,
    ) -> devops_20210625_models.GetPipelineArtifactUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_artifact_url_with_options(organization_id, request, headers, runtime)

    async def get_pipeline_artifact_url_async(
        self,
        organization_id: str,
        request: devops_20210625_models.GetPipelineArtifactUrlRequest,
    ) -> devops_20210625_models.GetPipelineArtifactUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_artifact_url_with_options_async(organization_id, request, headers, runtime)

    def get_pipeline_emas_artifact_url_with_options(
        self,
        organization_id: str,
        emas_job_instance_id: str,
        md_5: str,
        pipeline_id: str,
        pipeline_run_id: str,
        request: devops_20210625_models.GetPipelineEmasArtifactUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineEmasArtifactUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_connection_id):
            query['serviceConnectionId'] = request.service_connection_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPipelineEmasArtifactUrl',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRun/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/emas/artifact/{OpenApiUtilClient.get_encode_param(emas_job_instance_id)}/{OpenApiUtilClient.get_encode_param(md_5)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineEmasArtifactUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_emas_artifact_url_with_options_async(
        self,
        organization_id: str,
        emas_job_instance_id: str,
        md_5: str,
        pipeline_id: str,
        pipeline_run_id: str,
        request: devops_20210625_models.GetPipelineEmasArtifactUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineEmasArtifactUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_connection_id):
            query['serviceConnectionId'] = request.service_connection_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPipelineEmasArtifactUrl',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRun/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/emas/artifact/{OpenApiUtilClient.get_encode_param(emas_job_instance_id)}/{OpenApiUtilClient.get_encode_param(md_5)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineEmasArtifactUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_emas_artifact_url(
        self,
        organization_id: str,
        emas_job_instance_id: str,
        md_5: str,
        pipeline_id: str,
        pipeline_run_id: str,
        request: devops_20210625_models.GetPipelineEmasArtifactUrlRequest,
    ) -> devops_20210625_models.GetPipelineEmasArtifactUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_emas_artifact_url_with_options(organization_id, emas_job_instance_id, md_5, pipeline_id, pipeline_run_id, request, headers, runtime)

    async def get_pipeline_emas_artifact_url_async(
        self,
        organization_id: str,
        emas_job_instance_id: str,
        md_5: str,
        pipeline_id: str,
        pipeline_run_id: str,
        request: devops_20210625_models.GetPipelineEmasArtifactUrlRequest,
    ) -> devops_20210625_models.GetPipelineEmasArtifactUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_emas_artifact_url_with_options_async(organization_id, emas_job_instance_id, md_5, pipeline_id, pipeline_run_id, request, headers, runtime)

    def get_pipeline_group_with_options(
        self,
        organization_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_group_with_options_async(
        self,
        organization_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_group(
        self,
        organization_id: str,
        group_id: str,
    ) -> devops_20210625_models.GetPipelineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_group_with_options(organization_id, group_id, headers, runtime)

    async def get_pipeline_group_async(
        self,
        organization_id: str,
        group_id: str,
    ) -> devops_20210625_models.GetPipelineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_group_with_options_async(organization_id, group_id, headers, runtime)

    def get_pipeline_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_run(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
    ) -> devops_20210625_models.GetPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_run_with_options(organization_id, pipeline_id, pipeline_run_id, headers, runtime)

    async def get_pipeline_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
    ) -> devops_20210625_models.GetPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_run_with_options_async(organization_id, pipeline_id, pipeline_run_id, headers, runtime)

    def get_pipeline_scan_report_url_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.GetPipelineScanReportUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineScanReportUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.report_path):
            body['reportPath'] = request.report_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPipelineScanReportUrl',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/getPipelineScanReportUrl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineScanReportUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_scan_report_url_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.GetPipelineScanReportUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineScanReportUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.report_path):
            body['reportPath'] = request.report_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPipelineScanReportUrl',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/getPipelineScanReportUrl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineScanReportUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_scan_report_url(
        self,
        organization_id: str,
        request: devops_20210625_models.GetPipelineScanReportUrlRequest,
    ) -> devops_20210625_models.GetPipelineScanReportUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_scan_report_url_with_options(organization_id, request, headers, runtime)

    async def get_pipeline_scan_report_url_async(
        self,
        organization_id: str,
        request: devops_20210625_models.GetPipelineScanReportUrlRequest,
    ) -> devops_20210625_models.GetPipelineScanReportUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_scan_report_url_with_options_async(organization_id, request, headers, runtime)

    def get_project_info_with_options(
        self,
        organization_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetProjectInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/project/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetProjectInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_info_with_options_async(
        self,
        organization_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetProjectInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/project/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetProjectInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_info(
        self,
        organization_id: str,
        project_id: str,
    ) -> devops_20210625_models.GetProjectInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_info_with_options(organization_id, project_id, headers, runtime)

    async def get_project_info_async(
        self,
        organization_id: str,
        project_id: str,
    ) -> devops_20210625_models.GetProjectInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_info_with_options_async(organization_id, project_id, headers, runtime)

    def get_project_member_with_options(
        self,
        repository_id: str,
        aliyun_pk: str,
        request: devops_20210625_models.GetProjectMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetProjectMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/members/get/{OpenApiUtilClient.get_encode_param(aliyun_pk)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetProjectMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_member_with_options_async(
        self,
        repository_id: str,
        aliyun_pk: str,
        request: devops_20210625_models.GetProjectMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetProjectMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/members/get/{OpenApiUtilClient.get_encode_param(aliyun_pk)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetProjectMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_member(
        self,
        repository_id: str,
        aliyun_pk: str,
        request: devops_20210625_models.GetProjectMemberRequest,
    ) -> devops_20210625_models.GetProjectMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_member_with_options(repository_id, aliyun_pk, request, headers, runtime)

    async def get_project_member_async(
        self,
        repository_id: str,
        aliyun_pk: str,
        request: devops_20210625_models.GetProjectMemberRequest,
    ) -> devops_20210625_models.GetProjectMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_member_with_options_async(repository_id, aliyun_pk, request, headers, runtime)

    def get_push_rule_with_options(
        self,
        repository_id: str,
        push_rule_id: str,
        request: devops_20210625_models.GetPushRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPushRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPushRule',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/push_rule/{OpenApiUtilClient.get_encode_param(push_rule_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPushRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_push_rule_with_options_async(
        self,
        repository_id: str,
        push_rule_id: str,
        request: devops_20210625_models.GetPushRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPushRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPushRule',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/push_rule/{OpenApiUtilClient.get_encode_param(push_rule_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPushRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_push_rule(
        self,
        repository_id: str,
        push_rule_id: str,
        request: devops_20210625_models.GetPushRuleRequest,
    ) -> devops_20210625_models.GetPushRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_push_rule_with_options(repository_id, push_rule_id, request, headers, runtime)

    async def get_push_rule_async(
        self,
        repository_id: str,
        push_rule_id: str,
        request: devops_20210625_models.GetPushRuleRequest,
    ) -> devops_20210625_models.GetPushRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_push_rule_with_options_async(repository_id, push_rule_id, request, headers, runtime)

    def get_repository_with_options(
        self,
        request: devops_20210625_models.GetRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.identity):
            query['identity'] = request.identity
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/get',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repository_with_options_async(
        self,
        request: devops_20210625_models.GetRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.identity):
            query['identity'] = request.identity
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/get',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repository(
        self,
        request: devops_20210625_models.GetRepositoryRequest,
    ) -> devops_20210625_models.GetRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repository_with_options(request, headers, runtime)

    async def get_repository_async(
        self,
        request: devops_20210625_models.GetRepositoryRequest,
    ) -> devops_20210625_models.GetRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repository_with_options_async(request, headers, runtime)

    def get_repository_commit_with_options(
        self,
        repository_id: str,
        sha: str,
        request: devops_20210625_models.GetRepositoryCommitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetRepositoryCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.show_signature):
            query['showSignature'] = request.show_signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepositoryCommit',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/commits/{OpenApiUtilClient.get_encode_param(sha)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetRepositoryCommitResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repository_commit_with_options_async(
        self,
        repository_id: str,
        sha: str,
        request: devops_20210625_models.GetRepositoryCommitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetRepositoryCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.show_signature):
            query['showSignature'] = request.show_signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepositoryCommit',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/commits/{OpenApiUtilClient.get_encode_param(sha)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetRepositoryCommitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repository_commit(
        self,
        repository_id: str,
        sha: str,
        request: devops_20210625_models.GetRepositoryCommitRequest,
    ) -> devops_20210625_models.GetRepositoryCommitResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repository_commit_with_options(repository_id, sha, request, headers, runtime)

    async def get_repository_commit_async(
        self,
        repository_id: str,
        sha: str,
        request: devops_20210625_models.GetRepositoryCommitRequest,
    ) -> devops_20210625_models.GetRepositoryCommitResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repository_commit_with_options_async(repository_id, sha, request, headers, runtime)

    def get_repository_tag_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.GetRepositoryTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetRepositoryTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.tag_name):
            query['tagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepositoryTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/tag/info',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetRepositoryTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repository_tag_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.GetRepositoryTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetRepositoryTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.tag_name):
            query['tagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepositoryTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/tag/info',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetRepositoryTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repository_tag(
        self,
        repository_id: str,
        request: devops_20210625_models.GetRepositoryTagRequest,
    ) -> devops_20210625_models.GetRepositoryTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repository_tag_with_options(repository_id, request, headers, runtime)

    async def get_repository_tag_async(
        self,
        repository_id: str,
        request: devops_20210625_models.GetRepositoryTagRequest,
    ) -> devops_20210625_models.GetRepositoryTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repository_tag_with_options_async(repository_id, request, headers, runtime)

    def get_search_code_preview_with_options(
        self,
        request: devops_20210625_models.GetSearchCodePreviewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetSearchCodePreviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.doc_id):
            query['docId'] = request.doc_id
        if not UtilClient.is_unset(request.is_dsl):
            query['isDsl'] = request.is_dsl
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSearchCodePreview',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/search/code_preview',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetSearchCodePreviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_search_code_preview_with_options_async(
        self,
        request: devops_20210625_models.GetSearchCodePreviewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetSearchCodePreviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.doc_id):
            query['docId'] = request.doc_id
        if not UtilClient.is_unset(request.is_dsl):
            query['isDsl'] = request.is_dsl
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSearchCodePreview',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/search/code_preview',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetSearchCodePreviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_search_code_preview(
        self,
        request: devops_20210625_models.GetSearchCodePreviewRequest,
    ) -> devops_20210625_models.GetSearchCodePreviewResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_search_code_preview_with_options(request, headers, runtime)

    async def get_search_code_preview_async(
        self,
        request: devops_20210625_models.GetSearchCodePreviewRequest,
    ) -> devops_20210625_models.GetSearchCodePreviewResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_search_code_preview_with_options_async(request, headers, runtime)

    def get_sprint_info_with_options(
        self,
        organization_id: str,
        sprint_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetSprintInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSprintInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/sprints/{OpenApiUtilClient.get_encode_param(sprint_id)}/getSprintinfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetSprintInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sprint_info_with_options_async(
        self,
        organization_id: str,
        sprint_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetSprintInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSprintInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/sprints/{OpenApiUtilClient.get_encode_param(sprint_id)}/getSprintinfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetSprintInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sprint_info(
        self,
        organization_id: str,
        sprint_id: str,
    ) -> devops_20210625_models.GetSprintInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_sprint_info_with_options(organization_id, sprint_id, headers, runtime)

    async def get_sprint_info_async(
        self,
        organization_id: str,
        sprint_id: str,
    ) -> devops_20210625_models.GetSprintInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_sprint_info_with_options_async(organization_id, sprint_id, headers, runtime)

    def get_test_result_list_with_options(
        self,
        organization_id: str,
        test_plan_identifier: str,
        request: devops_20210625_models.GetTestResultListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetTestResultListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conditions):
            body['conditions'] = request.conditions
        if not UtilClient.is_unset(request.directory_identifier):
            body['directoryIdentifier'] = request.directory_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTestResultList',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/testhub/testplan/{OpenApiUtilClient.get_encode_param(test_plan_identifier)}/testresults',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetTestResultListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_test_result_list_with_options_async(
        self,
        organization_id: str,
        test_plan_identifier: str,
        request: devops_20210625_models.GetTestResultListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetTestResultListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conditions):
            body['conditions'] = request.conditions
        if not UtilClient.is_unset(request.directory_identifier):
            body['directoryIdentifier'] = request.directory_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTestResultList',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/testhub/testplan/{OpenApiUtilClient.get_encode_param(test_plan_identifier)}/testresults',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetTestResultListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_test_result_list(
        self,
        organization_id: str,
        test_plan_identifier: str,
        request: devops_20210625_models.GetTestResultListRequest,
    ) -> devops_20210625_models.GetTestResultListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_test_result_list_with_options(organization_id, test_plan_identifier, request, headers, runtime)

    async def get_test_result_list_async(
        self,
        organization_id: str,
        test_plan_identifier: str,
        request: devops_20210625_models.GetTestResultListRequest,
    ) -> devops_20210625_models.GetTestResultListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_test_result_list_with_options_async(organization_id, test_plan_identifier, request, headers, runtime)

    def get_testcase_list_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.GetTestcaseListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetTestcaseListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conditions):
            body['conditions'] = request.conditions
        if not UtilClient.is_unset(request.directory_identifier):
            body['directoryIdentifier'] = request.directory_identifier
        if not UtilClient.is_unset(request.max_result):
            body['maxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.space_identifier):
            body['spaceIdentifier'] = request.space_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTestcaseList',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/testhub/testcases',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetTestcaseListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_testcase_list_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.GetTestcaseListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetTestcaseListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conditions):
            body['conditions'] = request.conditions
        if not UtilClient.is_unset(request.directory_identifier):
            body['directoryIdentifier'] = request.directory_identifier
        if not UtilClient.is_unset(request.max_result):
            body['maxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.space_identifier):
            body['spaceIdentifier'] = request.space_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTestcaseList',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/testhub/testcases',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetTestcaseListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_testcase_list(
        self,
        organization_id: str,
        request: devops_20210625_models.GetTestcaseListRequest,
    ) -> devops_20210625_models.GetTestcaseListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_testcase_list_with_options(organization_id, request, headers, runtime)

    async def get_testcase_list_async(
        self,
        organization_id: str,
        request: devops_20210625_models.GetTestcaseListRequest,
    ) -> devops_20210625_models.GetTestcaseListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_testcase_list_with_options_async(organization_id, request, headers, runtime)

    def get_user_info_with_options(
        self,
        request: devops_20210625_models.GetUserInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetUserInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/users/current',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_info_with_options_async(
        self,
        request: devops_20210625_models.GetUserInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetUserInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/users/current',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_info(
        self,
        request: devops_20210625_models.GetUserInfoRequest,
    ) -> devops_20210625_models.GetUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_info_with_options(request, headers, runtime)

    async def get_user_info_async(
        self,
        request: devops_20210625_models.GetUserInfoRequest,
    ) -> devops_20210625_models.GetUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_info_with_options_async(request, headers, runtime)

    def get_vmdeploy_order_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetVMDeployOrderResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetVMDeployOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vmdeploy_order_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetVMDeployOrderResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetVMDeployOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vmdeploy_order(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
    ) -> devops_20210625_models.GetVMDeployOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_vmdeploy_order_with_options(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    async def get_vmdeploy_order_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
    ) -> devops_20210625_models.GetVMDeployOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_vmdeploy_order_with_options_async(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    def get_variable_group_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetVariableGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/variableGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetVariableGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_variable_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetVariableGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/variableGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetVariableGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_variable_group(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.GetVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_variable_group_with_options(organization_id, id, headers, runtime)

    async def get_variable_group_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.GetVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_variable_group_with_options_async(organization_id, id, headers, runtime)

    def get_work_item_activity_with_options(
        self,
        organization_id: str,
        workitem_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkItemActivityResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkItemActivity',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/getActivity',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkItemActivityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_work_item_activity_with_options_async(
        self,
        organization_id: str,
        workitem_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkItemActivityResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkItemActivity',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/getActivity',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkItemActivityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_work_item_activity(
        self,
        organization_id: str,
        workitem_id: str,
    ) -> devops_20210625_models.GetWorkItemActivityResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_work_item_activity_with_options(organization_id, workitem_id, headers, runtime)

    async def get_work_item_activity_async(
        self,
        organization_id: str,
        workitem_id: str,
    ) -> devops_20210625_models.GetWorkItemActivityResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_work_item_activity_with_options_async(organization_id, workitem_id, headers, runtime)

    def get_work_item_info_with_options(
        self,
        organization_id: str,
        workitem_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkItemInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkItemInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkItemInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_work_item_info_with_options_async(
        self,
        organization_id: str,
        workitem_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkItemInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkItemInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkItemInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_work_item_info(
        self,
        organization_id: str,
        workitem_id: str,
    ) -> devops_20210625_models.GetWorkItemInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_work_item_info_with_options(organization_id, workitem_id, headers, runtime)

    async def get_work_item_info_async(
        self,
        organization_id: str,
        workitem_id: str,
    ) -> devops_20210625_models.GetWorkItemInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_work_item_info_with_options_async(organization_id, workitem_id, headers, runtime)

    def get_work_item_work_flow_info_with_options(
        self,
        organization_id: str,
        workitem_id: str,
        request: devops_20210625_models.GetWorkItemWorkFlowInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkItemWorkFlowInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.configuration_id):
            query['configurationId'] = request.configuration_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkItemWorkFlowInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/getWorkflowInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkItemWorkFlowInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_work_item_work_flow_info_with_options_async(
        self,
        organization_id: str,
        workitem_id: str,
        request: devops_20210625_models.GetWorkItemWorkFlowInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkItemWorkFlowInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.configuration_id):
            query['configurationId'] = request.configuration_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkItemWorkFlowInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/getWorkflowInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkItemWorkFlowInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_work_item_work_flow_info(
        self,
        organization_id: str,
        workitem_id: str,
        request: devops_20210625_models.GetWorkItemWorkFlowInfoRequest,
    ) -> devops_20210625_models.GetWorkItemWorkFlowInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_work_item_work_flow_info_with_options(organization_id, workitem_id, request, headers, runtime)

    async def get_work_item_work_flow_info_async(
        self,
        organization_id: str,
        workitem_id: str,
        request: devops_20210625_models.GetWorkItemWorkFlowInfoRequest,
    ) -> devops_20210625_models.GetWorkItemWorkFlowInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_work_item_work_flow_info_with_options_async(organization_id, workitem_id, request, headers, runtime)

    def get_workitem_attachment_createmeta_with_options(
        self,
        organization_id: str,
        workitem_identifier: str,
        request: devops_20210625_models.GetWorkitemAttachmentCreatemetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkitemAttachmentCreatemetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkitemAttachmentCreatemeta',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitem/{OpenApiUtilClient.get_encode_param(workitem_identifier)}/attachment/createmeta',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkitemAttachmentCreatemetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workitem_attachment_createmeta_with_options_async(
        self,
        organization_id: str,
        workitem_identifier: str,
        request: devops_20210625_models.GetWorkitemAttachmentCreatemetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkitemAttachmentCreatemetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkitemAttachmentCreatemeta',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitem/{OpenApiUtilClient.get_encode_param(workitem_identifier)}/attachment/createmeta',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkitemAttachmentCreatemetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workitem_attachment_createmeta(
        self,
        organization_id: str,
        workitem_identifier: str,
        request: devops_20210625_models.GetWorkitemAttachmentCreatemetaRequest,
    ) -> devops_20210625_models.GetWorkitemAttachmentCreatemetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workitem_attachment_createmeta_with_options(organization_id, workitem_identifier, request, headers, runtime)

    async def get_workitem_attachment_createmeta_async(
        self,
        organization_id: str,
        workitem_identifier: str,
        request: devops_20210625_models.GetWorkitemAttachmentCreatemetaRequest,
    ) -> devops_20210625_models.GetWorkitemAttachmentCreatemetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_workitem_attachment_createmeta_with_options_async(organization_id, workitem_identifier, request, headers, runtime)

    def get_workitem_comment_list_with_options(
        self,
        organization_id: str,
        workitem_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkitemCommentListResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkitemCommentList',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/commentList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkitemCommentListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workitem_comment_list_with_options_async(
        self,
        organization_id: str,
        workitem_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkitemCommentListResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkitemCommentList',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/commentList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkitemCommentListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workitem_comment_list(
        self,
        organization_id: str,
        workitem_id: str,
    ) -> devops_20210625_models.GetWorkitemCommentListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workitem_comment_list_with_options(organization_id, workitem_id, headers, runtime)

    async def get_workitem_comment_list_async(
        self,
        organization_id: str,
        workitem_id: str,
    ) -> devops_20210625_models.GetWorkitemCommentListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_workitem_comment_list_with_options_async(organization_id, workitem_id, headers, runtime)

    def get_workitem_file_with_options(
        self,
        organization_id: str,
        workitem_identifier: str,
        file_identifier: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkitemFileResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkitemFile',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitem/{OpenApiUtilClient.get_encode_param(workitem_identifier)}/files/{OpenApiUtilClient.get_encode_param(file_identifier)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkitemFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workitem_file_with_options_async(
        self,
        organization_id: str,
        workitem_identifier: str,
        file_identifier: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkitemFileResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkitemFile',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitem/{OpenApiUtilClient.get_encode_param(workitem_identifier)}/files/{OpenApiUtilClient.get_encode_param(file_identifier)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkitemFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workitem_file(
        self,
        organization_id: str,
        workitem_identifier: str,
        file_identifier: str,
    ) -> devops_20210625_models.GetWorkitemFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workitem_file_with_options(organization_id, workitem_identifier, file_identifier, headers, runtime)

    async def get_workitem_file_async(
        self,
        organization_id: str,
        workitem_identifier: str,
        file_identifier: str,
    ) -> devops_20210625_models.GetWorkitemFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_workitem_file_with_options_async(organization_id, workitem_identifier, file_identifier, headers, runtime)

    def get_workitem_relations_with_options(
        self,
        organization_id: str,
        workitem_id: str,
        request: devops_20210625_models.GetWorkitemRelationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkitemRelationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.relation_type):
            query['relationType'] = request.relation_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkitemRelations',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/getRelations',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkitemRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workitem_relations_with_options_async(
        self,
        organization_id: str,
        workitem_id: str,
        request: devops_20210625_models.GetWorkitemRelationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkitemRelationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.relation_type):
            query['relationType'] = request.relation_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkitemRelations',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/getRelations',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkitemRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workitem_relations(
        self,
        organization_id: str,
        workitem_id: str,
        request: devops_20210625_models.GetWorkitemRelationsRequest,
    ) -> devops_20210625_models.GetWorkitemRelationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workitem_relations_with_options(organization_id, workitem_id, request, headers, runtime)

    async def get_workitem_relations_async(
        self,
        organization_id: str,
        workitem_id: str,
        request: devops_20210625_models.GetWorkitemRelationsRequest,
    ) -> devops_20210625_models.GetWorkitemRelationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_workitem_relations_with_options_async(organization_id, workitem_id, request, headers, runtime)

    def get_workitem_time_type_list_with_options(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkitemTimeTypeListResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkitemTimeTypeList',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/type/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkitemTimeTypeListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workitem_time_type_list_with_options_async(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkitemTimeTypeListResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkitemTimeTypeList',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/type/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkitemTimeTypeListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workitem_time_type_list(
        self,
        organization_id: str,
    ) -> devops_20210625_models.GetWorkitemTimeTypeListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workitem_time_type_list_with_options(organization_id, headers, runtime)

    async def get_workitem_time_type_list_async(
        self,
        organization_id: str,
    ) -> devops_20210625_models.GetWorkitemTimeTypeListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_workitem_time_type_list_with_options_async(organization_id, headers, runtime)

    def get_workspace_with_options(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkspaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workspace_with_options_async(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkspaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workspace(
        self,
        workspace_id: str,
    ) -> devops_20210625_models.GetWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workspace_with_options(workspace_id, headers, runtime)

    async def get_workspace_async(
        self,
        workspace_id: str,
    ) -> devops_20210625_models.GetWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_workspace_with_options_async(workspace_id, headers, runtime)

    def join_pipeline_group_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.JoinPipelineGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.JoinPipelineGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.pipeline_ids):
            query['pipelineIds'] = request.pipeline_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JoinPipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups/join',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.JoinPipelineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def join_pipeline_group_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.JoinPipelineGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.JoinPipelineGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.pipeline_ids):
            query['pipelineIds'] = request.pipeline_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JoinPipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups/join',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.JoinPipelineGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def join_pipeline_group(
        self,
        organization_id: str,
        request: devops_20210625_models.JoinPipelineGroupRequest,
    ) -> devops_20210625_models.JoinPipelineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.join_pipeline_group_with_options(organization_id, request, headers, runtime)

    async def join_pipeline_group_async(
        self,
        organization_id: str,
        request: devops_20210625_models.JoinPipelineGroupRequest,
    ) -> devops_20210625_models.JoinPipelineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.join_pipeline_group_with_options_async(organization_id, request, headers, runtime)

    def link_merge_request_label_with_options(
        self,
        request: devops_20210625_models.LinkMergeRequestLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.LinkMergeRequestLabelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.local_id):
            query['localId'] = request.local_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        body = {}
        if not UtilClient.is_unset(request.label_ids):
            body['labelIds'] = request.label_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LinkMergeRequestLabel',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/merge_requests/link_labels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.LinkMergeRequestLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def link_merge_request_label_with_options_async(
        self,
        request: devops_20210625_models.LinkMergeRequestLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.LinkMergeRequestLabelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.local_id):
            query['localId'] = request.local_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        body = {}
        if not UtilClient.is_unset(request.label_ids):
            body['labelIds'] = request.label_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LinkMergeRequestLabel',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/merge_requests/link_labels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.LinkMergeRequestLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def link_merge_request_label(
        self,
        request: devops_20210625_models.LinkMergeRequestLabelRequest,
    ) -> devops_20210625_models.LinkMergeRequestLabelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.link_merge_request_label_with_options(request, headers, runtime)

    async def link_merge_request_label_async(
        self,
        request: devops_20210625_models.LinkMergeRequestLabelRequest,
    ) -> devops_20210625_models.LinkMergeRequestLabelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.link_merge_request_label_with_options_async(request, headers, runtime)

    def list_application_members_with_options(
        self,
        app_name: str,
        request: devops_20210625_models.ListApplicationMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListApplicationMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/appstack/apps/{OpenApiUtilClient.get_encode_param(app_name)}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListApplicationMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_members_with_options_async(
        self,
        app_name: str,
        request: devops_20210625_models.ListApplicationMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListApplicationMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/appstack/apps/{OpenApiUtilClient.get_encode_param(app_name)}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListApplicationMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_members(
        self,
        app_name: str,
        request: devops_20210625_models.ListApplicationMembersRequest,
    ) -> devops_20210625_models.ListApplicationMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_application_members_with_options(app_name, request, headers, runtime)

    async def list_application_members_async(
        self,
        app_name: str,
        request: devops_20210625_models.ListApplicationMembersRequest,
    ) -> devops_20210625_models.ListApplicationMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_application_members_with_options_async(app_name, request, headers, runtime)

    def list_applications_with_options(
        self,
        request: devops_20210625_models.ListApplicationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListApplicationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.pagination):
            query['pagination'] = request.pagination
        if not UtilClient.is_unset(request.per_page):
            query['perPage'] = request.per_page
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplications',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/appstack/apps%3Asearch',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_with_options_async(
        self,
        request: devops_20210625_models.ListApplicationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListApplicationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.pagination):
            query['pagination'] = request.pagination
        if not UtilClient.is_unset(request.per_page):
            query['perPage'] = request.per_page
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplications',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/appstack/apps%3Asearch',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications(
        self,
        request: devops_20210625_models.ListApplicationsRequest,
    ) -> devops_20210625_models.ListApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_applications_with_options(request, headers, runtime)

    async def list_applications_async(
        self,
        request: devops_20210625_models.ListApplicationsRequest,
    ) -> devops_20210625_models.ListApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_applications_with_options_async(request, headers, runtime)

    def list_check_runs_with_options(
        self,
        request: devops_20210625_models.ListCheckRunsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListCheckRunsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.ref):
            query['ref'] = request.ref
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCheckRuns',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/check_runs/list_check_runs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListCheckRunsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_check_runs_with_options_async(
        self,
        request: devops_20210625_models.ListCheckRunsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListCheckRunsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.ref):
            query['ref'] = request.ref
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCheckRuns',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/check_runs/list_check_runs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListCheckRunsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_check_runs(
        self,
        request: devops_20210625_models.ListCheckRunsRequest,
    ) -> devops_20210625_models.ListCheckRunsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_check_runs_with_options(request, headers, runtime)

    async def list_check_runs_async(
        self,
        request: devops_20210625_models.ListCheckRunsRequest,
    ) -> devops_20210625_models.ListCheckRunsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_check_runs_with_options_async(request, headers, runtime)

    def list_commit_statuses_with_options(
        self,
        request: devops_20210625_models.ListCommitStatusesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListCommitStatusesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        if not UtilClient.is_unset(request.sha):
            query['sha'] = request.sha
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCommitStatuses',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/repository/commit_statuses/list_commit_statuses',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListCommitStatusesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_commit_statuses_with_options_async(
        self,
        request: devops_20210625_models.ListCommitStatusesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListCommitStatusesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        if not UtilClient.is_unset(request.sha):
            query['sha'] = request.sha
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCommitStatuses',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/repository/commit_statuses/list_commit_statuses',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListCommitStatusesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_commit_statuses(
        self,
        request: devops_20210625_models.ListCommitStatusesRequest,
    ) -> devops_20210625_models.ListCommitStatusesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_commit_statuses_with_options(request, headers, runtime)

    async def list_commit_statuses_async(
        self,
        request: devops_20210625_models.ListCommitStatusesRequest,
    ) -> devops_20210625_models.ListCommitStatusesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_commit_statuses_with_options_async(request, headers, runtime)

    def list_flow_tag_groups_with_options(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListFlowTagGroupsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFlowTagGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tagGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListFlowTagGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_tag_groups_with_options_async(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListFlowTagGroupsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFlowTagGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tagGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListFlowTagGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow_tag_groups(
        self,
        organization_id: str,
    ) -> devops_20210625_models.ListFlowTagGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_flow_tag_groups_with_options(organization_id, headers, runtime)

    async def list_flow_tag_groups_async(
        self,
        organization_id: str,
    ) -> devops_20210625_models.ListFlowTagGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_flow_tag_groups_with_options_async(organization_id, headers, runtime)

    def list_group_member_with_options(
        self,
        group_id: str,
        request: devops_20210625_models.ListGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/groups/{OpenApiUtilClient.get_encode_param(group_id)}/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_group_member_with_options_async(
        self,
        group_id: str,
        request: devops_20210625_models.ListGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/groups/{OpenApiUtilClient.get_encode_param(group_id)}/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_group_member(
        self,
        group_id: str,
        request: devops_20210625_models.ListGroupMemberRequest,
    ) -> devops_20210625_models.ListGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_group_member_with_options(group_id, request, headers, runtime)

    async def list_group_member_async(
        self,
        group_id: str,
        request: devops_20210625_models.ListGroupMemberRequest,
    ) -> devops_20210625_models.ListGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_group_member_with_options_async(group_id, request, headers, runtime)

    def list_group_repositories_with_options(
        self,
        group_id: str,
        request: devops_20210625_models.ListGroupRepositoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListGroupRepositoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupRepositories',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/groups/{OpenApiUtilClient.get_encode_param(group_id)}/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListGroupRepositoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_group_repositories_with_options_async(
        self,
        group_id: str,
        request: devops_20210625_models.ListGroupRepositoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListGroupRepositoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupRepositories',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/groups/{OpenApiUtilClient.get_encode_param(group_id)}/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListGroupRepositoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_group_repositories(
        self,
        group_id: str,
        request: devops_20210625_models.ListGroupRepositoriesRequest,
    ) -> devops_20210625_models.ListGroupRepositoriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_group_repositories_with_options(group_id, request, headers, runtime)

    async def list_group_repositories_async(
        self,
        group_id: str,
        request: devops_20210625_models.ListGroupRepositoriesRequest,
    ) -> devops_20210625_models.ListGroupRepositoriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_group_repositories_with_options_async(group_id, request, headers, runtime)

    def list_host_groups_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListHostGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListHostGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.creator_account_ids):
            query['creatorAccountIds'] = request.creator_account_ids
        if not UtilClient.is_unset(request.ids):
            query['ids'] = request.ids
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_order):
            query['pageOrder'] = request.page_order
        if not UtilClient.is_unset(request.page_sort):
            query['pageSort'] = request.page_sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/hostGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListHostGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_groups_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListHostGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListHostGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.creator_account_ids):
            query['creatorAccountIds'] = request.creator_account_ids
        if not UtilClient.is_unset(request.ids):
            query['ids'] = request.ids
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_order):
            query['pageOrder'] = request.page_order
        if not UtilClient.is_unset(request.page_sort):
            query['pageSort'] = request.page_sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/hostGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListHostGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_host_groups(
        self,
        organization_id: str,
        request: devops_20210625_models.ListHostGroupsRequest,
    ) -> devops_20210625_models.ListHostGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_host_groups_with_options(organization_id, request, headers, runtime)

    async def list_host_groups_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListHostGroupsRequest,
    ) -> devops_20210625_models.ListHostGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_host_groups_with_options_async(organization_id, request, headers, runtime)

    def list_joined_organizations_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListJoinedOrganizationsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListJoinedOrganizations',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/users/joinedOrgs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListJoinedOrganizationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_joined_organizations_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListJoinedOrganizationsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListJoinedOrganizations',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/users/joinedOrgs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListJoinedOrganizationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_joined_organizations(self) -> devops_20210625_models.ListJoinedOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_joined_organizations_with_options(headers, runtime)

    async def list_joined_organizations_async(self) -> devops_20210625_models.ListJoinedOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_joined_organizations_with_options_async(headers, runtime)

    def list_merge_request_comments_with_options(
        self,
        request: devops_20210625_models.ListMergeRequestCommentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListMergeRequestCommentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.local_id):
            query['localId'] = request.local_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        body = {}
        if not UtilClient.is_unset(request.comment_type):
            body['commentType'] = request.comment_type
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        if not UtilClient.is_unset(request.patch_set_biz_ids):
            body['patchSetBizIds'] = request.patch_set_biz_ids
        if not UtilClient.is_unset(request.resolved):
            body['resolved'] = request.resolved
        if not UtilClient.is_unset(request.state):
            body['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMergeRequestComments',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/merge_requests/comments/list_comments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListMergeRequestCommentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_merge_request_comments_with_options_async(
        self,
        request: devops_20210625_models.ListMergeRequestCommentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListMergeRequestCommentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.local_id):
            query['localId'] = request.local_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        body = {}
        if not UtilClient.is_unset(request.comment_type):
            body['commentType'] = request.comment_type
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        if not UtilClient.is_unset(request.patch_set_biz_ids):
            body['patchSetBizIds'] = request.patch_set_biz_ids
        if not UtilClient.is_unset(request.resolved):
            body['resolved'] = request.resolved
        if not UtilClient.is_unset(request.state):
            body['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMergeRequestComments',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/merge_requests/comments/list_comments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListMergeRequestCommentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_merge_request_comments(
        self,
        request: devops_20210625_models.ListMergeRequestCommentsRequest,
    ) -> devops_20210625_models.ListMergeRequestCommentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_merge_request_comments_with_options(request, headers, runtime)

    async def list_merge_request_comments_async(
        self,
        request: devops_20210625_models.ListMergeRequestCommentsRequest,
    ) -> devops_20210625_models.ListMergeRequestCommentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_merge_request_comments_with_options_async(request, headers, runtime)

    def list_merge_request_files_reads_with_options(
        self,
        request: devops_20210625_models.ListMergeRequestFilesReadsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListMergeRequestFilesReadsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.from_patch_set_biz_id):
            query['fromPatchSetBizId'] = request.from_patch_set_biz_id
        if not UtilClient.is_unset(request.local_id):
            query['localId'] = request.local_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        if not UtilClient.is_unset(request.to_patch_set_biz_id):
            query['toPatchSetBizId'] = request.to_patch_set_biz_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMergeRequestFilesReads',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/merge_requests/diffs/files_read_infos',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListMergeRequestFilesReadsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_merge_request_files_reads_with_options_async(
        self,
        request: devops_20210625_models.ListMergeRequestFilesReadsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListMergeRequestFilesReadsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.from_patch_set_biz_id):
            query['fromPatchSetBizId'] = request.from_patch_set_biz_id
        if not UtilClient.is_unset(request.local_id):
            query['localId'] = request.local_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        if not UtilClient.is_unset(request.to_patch_set_biz_id):
            query['toPatchSetBizId'] = request.to_patch_set_biz_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMergeRequestFilesReads',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/merge_requests/diffs/files_read_infos',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListMergeRequestFilesReadsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_merge_request_files_reads(
        self,
        request: devops_20210625_models.ListMergeRequestFilesReadsRequest,
    ) -> devops_20210625_models.ListMergeRequestFilesReadsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_merge_request_files_reads_with_options(request, headers, runtime)

    async def list_merge_request_files_reads_async(
        self,
        request: devops_20210625_models.ListMergeRequestFilesReadsRequest,
    ) -> devops_20210625_models.ListMergeRequestFilesReadsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_merge_request_files_reads_with_options_async(request, headers, runtime)

    def list_merge_request_labels_with_options(
        self,
        request: devops_20210625_models.ListMergeRequestLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListMergeRequestLabelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.local_id):
            query['localId'] = request.local_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMergeRequestLabels',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/merge_requests/labels',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListMergeRequestLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_merge_request_labels_with_options_async(
        self,
        request: devops_20210625_models.ListMergeRequestLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListMergeRequestLabelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.local_id):
            query['localId'] = request.local_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMergeRequestLabels',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/merge_requests/labels',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListMergeRequestLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_merge_request_labels(
        self,
        request: devops_20210625_models.ListMergeRequestLabelsRequest,
    ) -> devops_20210625_models.ListMergeRequestLabelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_merge_request_labels_with_options(request, headers, runtime)

    async def list_merge_request_labels_async(
        self,
        request: devops_20210625_models.ListMergeRequestLabelsRequest,
    ) -> devops_20210625_models.ListMergeRequestLabelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_merge_request_labels_with_options_async(request, headers, runtime)

    def list_merge_request_patch_sets_with_options(
        self,
        request: devops_20210625_models.ListMergeRequestPatchSetsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListMergeRequestPatchSetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.local_id):
            query['localId'] = request.local_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMergeRequestPatchSets',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/merge_requests/diffs/list_patchsets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListMergeRequestPatchSetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_merge_request_patch_sets_with_options_async(
        self,
        request: devops_20210625_models.ListMergeRequestPatchSetsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListMergeRequestPatchSetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.local_id):
            query['localId'] = request.local_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMergeRequestPatchSets',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/merge_requests/diffs/list_patchsets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListMergeRequestPatchSetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_merge_request_patch_sets(
        self,
        request: devops_20210625_models.ListMergeRequestPatchSetsRequest,
    ) -> devops_20210625_models.ListMergeRequestPatchSetsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_merge_request_patch_sets_with_options(request, headers, runtime)

    async def list_merge_request_patch_sets_async(
        self,
        request: devops_20210625_models.ListMergeRequestPatchSetsRequest,
    ) -> devops_20210625_models.ListMergeRequestPatchSetsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_merge_request_patch_sets_with_options_async(request, headers, runtime)

    def list_merge_requests_with_options(
        self,
        request: devops_20210625_models.ListMergeRequestsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListMergeRequestsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.author_ids):
            query['authorIds'] = request.author_ids
        if not UtilClient.is_unset(request.created_after):
            query['createdAfter'] = request.created_after
        if not UtilClient.is_unset(request.created_before):
            query['createdBefore'] = request.created_before
        if not UtilClient.is_unset(request.filter):
            query['filter'] = request.filter
        if not UtilClient.is_unset(request.group_ids):
            query['groupIds'] = request.group_ids
        if not UtilClient.is_unset(request.label_ids):
            query['labelIds'] = request.label_ids
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_ids):
            query['projectIds'] = request.project_ids
        if not UtilClient.is_unset(request.reviewer_ids):
            query['reviewerIds'] = request.reviewer_ids
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMergeRequests',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/merge_requests/advanced_search',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListMergeRequestsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_merge_requests_with_options_async(
        self,
        request: devops_20210625_models.ListMergeRequestsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListMergeRequestsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.author_ids):
            query['authorIds'] = request.author_ids
        if not UtilClient.is_unset(request.created_after):
            query['createdAfter'] = request.created_after
        if not UtilClient.is_unset(request.created_before):
            query['createdBefore'] = request.created_before
        if not UtilClient.is_unset(request.filter):
            query['filter'] = request.filter
        if not UtilClient.is_unset(request.group_ids):
            query['groupIds'] = request.group_ids
        if not UtilClient.is_unset(request.label_ids):
            query['labelIds'] = request.label_ids
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_ids):
            query['projectIds'] = request.project_ids
        if not UtilClient.is_unset(request.reviewer_ids):
            query['reviewerIds'] = request.reviewer_ids
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMergeRequests',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/merge_requests/advanced_search',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListMergeRequestsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_merge_requests(
        self,
        request: devops_20210625_models.ListMergeRequestsRequest,
    ) -> devops_20210625_models.ListMergeRequestsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_merge_requests_with_options(request, headers, runtime)

    async def list_merge_requests_async(
        self,
        request: devops_20210625_models.ListMergeRequestsRequest,
    ) -> devops_20210625_models.ListMergeRequestsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_merge_requests_with_options_async(request, headers, runtime)

    def list_organization_members_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListOrganizationMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListOrganizationMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contains_extern_info):
            query['containsExternInfo'] = request.contains_extern_info
        if not UtilClient.is_unset(request.extern_uid):
            query['externUid'] = request.extern_uid
        if not UtilClient.is_unset(request.join_time_from):
            query['joinTimeFrom'] = request.join_time_from
        if not UtilClient.is_unset(request.join_time_to):
            query['joinTimeTo'] = request.join_time_to
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.organization_member_name):
            query['organizationMemberName'] = request.organization_member_name
        if not UtilClient.is_unset(request.provider):
            query['provider'] = request.provider
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListOrganizationMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_organization_members_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListOrganizationMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListOrganizationMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contains_extern_info):
            query['containsExternInfo'] = request.contains_extern_info
        if not UtilClient.is_unset(request.extern_uid):
            query['externUid'] = request.extern_uid
        if not UtilClient.is_unset(request.join_time_from):
            query['joinTimeFrom'] = request.join_time_from
        if not UtilClient.is_unset(request.join_time_to):
            query['joinTimeTo'] = request.join_time_to
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.organization_member_name):
            query['organizationMemberName'] = request.organization_member_name
        if not UtilClient.is_unset(request.provider):
            query['provider'] = request.provider
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListOrganizationMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_organization_members(
        self,
        organization_id: str,
        request: devops_20210625_models.ListOrganizationMembersRequest,
    ) -> devops_20210625_models.ListOrganizationMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_organization_members_with_options(organization_id, request, headers, runtime)

    async def list_organization_members_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListOrganizationMembersRequest,
    ) -> devops_20210625_models.ListOrganizationMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_organization_members_with_options_async(organization_id, request, headers, runtime)

    def list_organizations_with_options(
        self,
        request: devops_20210625_models.ListOrganizationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListOrganizationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_level):
            query['accessLevel'] = request.access_level
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.min_access_level):
            query['minAccessLevel'] = request.min_access_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizations',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organizations/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListOrganizationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_organizations_with_options_async(
        self,
        request: devops_20210625_models.ListOrganizationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListOrganizationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_level):
            query['accessLevel'] = request.access_level
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.min_access_level):
            query['minAccessLevel'] = request.min_access_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizations',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organizations/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListOrganizationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_organizations(
        self,
        request: devops_20210625_models.ListOrganizationsRequest,
    ) -> devops_20210625_models.ListOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_organizations_with_options(request, headers, runtime)

    async def list_organizations_async(
        self,
        request: devops_20210625_models.ListOrganizationsRequest,
    ) -> devops_20210625_models.ListOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_organizations_with_options_async(request, headers, runtime)

    def list_pipeline_group_pipelines_with_options(
        self,
        organization_id: str,
        group_id: str,
        request: devops_20210625_models.ListPipelineGroupPipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineGroupPipelinesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.execute_end_time):
            query['executeEndTime'] = request.execute_end_time
        if not UtilClient.is_unset(request.execute_start_time):
            query['executeStartTime'] = request.execute_start_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.result_status_list):
            query['resultStatusList'] = request.result_status_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineGroupPipelines',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups/{OpenApiUtilClient.get_encode_param(group_id)}/pipelines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineGroupPipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_group_pipelines_with_options_async(
        self,
        organization_id: str,
        group_id: str,
        request: devops_20210625_models.ListPipelineGroupPipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineGroupPipelinesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.execute_end_time):
            query['executeEndTime'] = request.execute_end_time
        if not UtilClient.is_unset(request.execute_start_time):
            query['executeStartTime'] = request.execute_start_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.result_status_list):
            query['resultStatusList'] = request.result_status_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineGroupPipelines',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups/{OpenApiUtilClient.get_encode_param(group_id)}/pipelines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineGroupPipelinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_group_pipelines(
        self,
        organization_id: str,
        group_id: str,
        request: devops_20210625_models.ListPipelineGroupPipelinesRequest,
    ) -> devops_20210625_models.ListPipelineGroupPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_group_pipelines_with_options(organization_id, group_id, request, headers, runtime)

    async def list_pipeline_group_pipelines_async(
        self,
        organization_id: str,
        group_id: str,
        request: devops_20210625_models.ListPipelineGroupPipelinesRequest,
    ) -> devops_20210625_models.ListPipelineGroupPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_group_pipelines_with_options_async(organization_id, group_id, request, headers, runtime)

    def list_pipeline_groups_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListPipelineGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_groups_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListPipelineGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_groups(
        self,
        organization_id: str,
        request: devops_20210625_models.ListPipelineGroupsRequest,
    ) -> devops_20210625_models.ListPipelineGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_groups_with_options(organization_id, request, headers, runtime)

    async def list_pipeline_groups_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListPipelineGroupsRequest,
    ) -> devops_20210625_models.ListPipelineGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_groups_with_options_async(organization_id, request, headers, runtime)

    def list_pipeline_job_historys_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineJobHistorysRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineJobHistorysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.identifier):
            query['identifier'] = request.identifier
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineJobHistorys',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/{OpenApiUtilClient.get_encode_param(pipeline_id)}/job/historys',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineJobHistorysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_job_historys_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineJobHistorysRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineJobHistorysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.identifier):
            query['identifier'] = request.identifier
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineJobHistorys',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/{OpenApiUtilClient.get_encode_param(pipeline_id)}/job/historys',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineJobHistorysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_job_historys(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineJobHistorysRequest,
    ) -> devops_20210625_models.ListPipelineJobHistorysResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_job_historys_with_options(organization_id, pipeline_id, request, headers, runtime)

    async def list_pipeline_job_historys_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineJobHistorysRequest,
    ) -> devops_20210625_models.ListPipelineJobHistorysResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_job_historys_with_options_async(organization_id, pipeline_id, request, headers, runtime)

    def list_pipeline_jobs_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineJobs',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/{OpenApiUtilClient.get_encode_param(pipeline_id)}/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_jobs_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineJobs',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/{OpenApiUtilClient.get_encode_param(pipeline_id)}/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_jobs(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineJobsRequest,
    ) -> devops_20210625_models.ListPipelineJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_jobs_with_options(organization_id, pipeline_id, request, headers, runtime)

    async def list_pipeline_jobs_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineJobsRequest,
    ) -> devops_20210625_models.ListPipelineJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_jobs_with_options_async(organization_id, pipeline_id, request, headers, runtime)

    def list_pipeline_relations_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineRelationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineRelationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rel_object_type):
            query['relObjectType'] = request.rel_object_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineRelations',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRelations',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_relations_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineRelationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineRelationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rel_object_type):
            query['relObjectType'] = request.rel_object_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineRelations',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRelations',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_relations(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineRelationsRequest,
    ) -> devops_20210625_models.ListPipelineRelationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_relations_with_options(organization_id, pipeline_id, request, headers, runtime)

    async def list_pipeline_relations_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineRelationsRequest,
    ) -> devops_20210625_models.ListPipelineRelationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_relations_with_options_async(organization_id, pipeline_id, request, headers, runtime)

    def list_pipeline_runs_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineRunsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineRunsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.trigger_mode):
            query['triggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineRuns',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineRunsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_runs_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineRunsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineRunsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.trigger_mode):
            query['triggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineRuns',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineRunsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_runs(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineRunsRequest,
    ) -> devops_20210625_models.ListPipelineRunsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_runs_with_options(organization_id, pipeline_id, request, headers, runtime)

    async def list_pipeline_runs_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineRunsRequest,
    ) -> devops_20210625_models.ListPipelineRunsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_runs_with_options_async(organization_id, pipeline_id, request, headers, runtime)

    def list_pipelines_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListPipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelinesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.creator_account_ids):
            query['creatorAccountIds'] = request.creator_account_ids
        if not UtilClient.is_unset(request.execute_account_ids):
            query['executeAccountIds'] = request.execute_account_ids
        if not UtilClient.is_unset(request.execute_end_time):
            query['executeEndTime'] = request.execute_end_time
        if not UtilClient.is_unset(request.execute_start_time):
            query['executeStartTime'] = request.execute_start_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.status_list):
            query['statusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelines',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipelines_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListPipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelinesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.creator_account_ids):
            query['creatorAccountIds'] = request.creator_account_ids
        if not UtilClient.is_unset(request.execute_account_ids):
            query['executeAccountIds'] = request.execute_account_ids
        if not UtilClient.is_unset(request.execute_end_time):
            query['executeEndTime'] = request.execute_end_time
        if not UtilClient.is_unset(request.execute_start_time):
            query['executeStartTime'] = request.execute_start_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.status_list):
            query['statusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelines',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipelines(
        self,
        organization_id: str,
        request: devops_20210625_models.ListPipelinesRequest,
    ) -> devops_20210625_models.ListPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipelines_with_options(organization_id, request, headers, runtime)

    async def list_pipelines_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListPipelinesRequest,
    ) -> devops_20210625_models.ListPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipelines_with_options_async(organization_id, request, headers, runtime)

    def list_project_labels_with_options(
        self,
        request: devops_20210625_models.ListProjectLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProjectLabelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        if not UtilClient.is_unset(request.with_counts):
            query['withCounts'] = request.with_counts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectLabels',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/labels',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_labels_with_options_async(
        self,
        request: devops_20210625_models.ListProjectLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProjectLabelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        if not UtilClient.is_unset(request.with_counts):
            query['withCounts'] = request.with_counts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectLabels',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/labels',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_labels(
        self,
        request: devops_20210625_models.ListProjectLabelsRequest,
    ) -> devops_20210625_models.ListProjectLabelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_labels_with_options(request, headers, runtime)

    async def list_project_labels_async(
        self,
        request: devops_20210625_models.ListProjectLabelsRequest,
    ) -> devops_20210625_models.ListProjectLabelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_project_labels_with_options_async(request, headers, runtime)

    def list_project_members_with_options(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.ListProjectMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProjectMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_type):
            query['targetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/listMembers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_members_with_options_async(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.ListProjectMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProjectMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_type):
            query['targetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/listMembers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_members(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.ListProjectMembersRequest,
    ) -> devops_20210625_models.ListProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_members_with_options(organization_id, project_id, request, headers, runtime)

    async def list_project_members_async(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.ListProjectMembersRequest,
    ) -> devops_20210625_models.ListProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_project_members_with_options_async(organization_id, project_id, request, headers, runtime)

    def list_project_templates_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListProjectTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProjectTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectTemplates',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/listTemplates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_templates_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListProjectTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProjectTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectTemplates',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/listTemplates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_templates(
        self,
        organization_id: str,
        request: devops_20210625_models.ListProjectTemplatesRequest,
    ) -> devops_20210625_models.ListProjectTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_templates_with_options(organization_id, request, headers, runtime)

    async def list_project_templates_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListProjectTemplatesRequest,
    ) -> devops_20210625_models.ListProjectTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_project_templates_with_options_async(organization_id, request, headers, runtime)

    def list_project_workitem_types_with_options(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.ListProjectWorkitemTypesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProjectWorkitemTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectWorkitemTypes',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/getWorkitemType',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectWorkitemTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_workitem_types_with_options_async(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.ListProjectWorkitemTypesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProjectWorkitemTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectWorkitemTypes',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/getWorkitemType',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectWorkitemTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_workitem_types(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.ListProjectWorkitemTypesRequest,
    ) -> devops_20210625_models.ListProjectWorkitemTypesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_workitem_types_with_options(organization_id, project_id, request, headers, runtime)

    async def list_project_workitem_types_async(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.ListProjectWorkitemTypesRequest,
    ) -> devops_20210625_models.ListProjectWorkitemTypesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_project_workitem_types_with_options_async(organization_id, project_id, request, headers, runtime)

    def list_projects_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.conditions):
            query['conditions'] = request.conditions
        if not UtilClient.is_unset(request.extra_conditions):
            query['extraConditions'] = request.extra_conditions
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.scope):
            query['scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/listProjects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.conditions):
            query['conditions'] = request.conditions
        if not UtilClient.is_unset(request.extra_conditions):
            query['extraConditions'] = request.extra_conditions
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.scope):
            query['scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/listProjects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        organization_id: str,
        request: devops_20210625_models.ListProjectsRequest,
    ) -> devops_20210625_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_projects_with_options(organization_id, request, headers, runtime)

    async def list_projects_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListProjectsRequest,
    ) -> devops_20210625_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_projects_with_options_async(organization_id, request, headers, runtime)

    def list_protected_branches_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.ListProtectedBranchesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProtectedBranchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProtectedBranches',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/protect_branches',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProtectedBranchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_protected_branches_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListProtectedBranchesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProtectedBranchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProtectedBranches',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/protect_branches',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProtectedBranchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_protected_branches(
        self,
        repository_id: str,
        request: devops_20210625_models.ListProtectedBranchesRequest,
    ) -> devops_20210625_models.ListProtectedBranchesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_protected_branches_with_options(repository_id, request, headers, runtime)

    async def list_protected_branches_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListProtectedBranchesRequest,
    ) -> devops_20210625_models.ListProtectedBranchesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_protected_branches_with_options_async(repository_id, request, headers, runtime)

    def list_push_rules_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.ListPushRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPushRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPushRules',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/push_rule/push_rules/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPushRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_push_rules_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListPushRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPushRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPushRules',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/push_rule/push_rules/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPushRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_push_rules(
        self,
        repository_id: str,
        request: devops_20210625_models.ListPushRulesRequest,
    ) -> devops_20210625_models.ListPushRulesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_push_rules_with_options(repository_id, request, headers, runtime)

    async def list_push_rules_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListPushRulesRequest,
    ) -> devops_20210625_models.ListPushRulesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_push_rules_with_options_async(repository_id, request, headers, runtime)

    def list_repositories_with_options(
        self,
        request: devops_20210625_models.ListRepositoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.archived):
            query['archived'] = request.archived
        if not UtilClient.is_unset(request.min_access_level):
            query['minAccessLevel'] = request.min_access_level
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.per_page):
            query['perPage'] = request.per_page
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositories',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repositories_with_options_async(
        self,
        request: devops_20210625_models.ListRepositoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.archived):
            query['archived'] = request.archived
        if not UtilClient.is_unset(request.min_access_level):
            query['minAccessLevel'] = request.min_access_level
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.per_page):
            query['perPage'] = request.per_page
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositories',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repositories(
        self,
        request: devops_20210625_models.ListRepositoriesRequest,
    ) -> devops_20210625_models.ListRepositoriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repositories_with_options(request, headers, runtime)

    async def list_repositories_async(
        self,
        request: devops_20210625_models.ListRepositoriesRequest,
    ) -> devops_20210625_models.ListRepositoriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repositories_with_options_async(request, headers, runtime)

    def list_repository_branches_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryBranchesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryBranchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryBranches',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/branches',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryBranchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repository_branches_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryBranchesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryBranchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryBranches',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/branches',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryBranchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repository_branches(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryBranchesRequest,
    ) -> devops_20210625_models.ListRepositoryBranchesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_branches_with_options(repository_id, request, headers, runtime)

    async def list_repository_branches_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryBranchesRequest,
    ) -> devops_20210625_models.ListRepositoryBranchesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_branches_with_options_async(repository_id, request, headers, runtime)

    def list_repository_commit_diff_with_options(
        self,
        repository_id: str,
        sha: str,
        request: devops_20210625_models.ListRepositoryCommitDiffRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryCommitDiffResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.context_line):
            query['contextLine'] = request.context_line
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryCommitDiff',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/commits/{OpenApiUtilClient.get_encode_param(sha)}/diff',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryCommitDiffResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repository_commit_diff_with_options_async(
        self,
        repository_id: str,
        sha: str,
        request: devops_20210625_models.ListRepositoryCommitDiffRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryCommitDiffResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.context_line):
            query['contextLine'] = request.context_line
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryCommitDiff',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/commits/{OpenApiUtilClient.get_encode_param(sha)}/diff',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryCommitDiffResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repository_commit_diff(
        self,
        repository_id: str,
        sha: str,
        request: devops_20210625_models.ListRepositoryCommitDiffRequest,
    ) -> devops_20210625_models.ListRepositoryCommitDiffResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_commit_diff_with_options(repository_id, sha, request, headers, runtime)

    async def list_repository_commit_diff_async(
        self,
        repository_id: str,
        sha: str,
        request: devops_20210625_models.ListRepositoryCommitDiffRequest,
    ) -> devops_20210625_models.ListRepositoryCommitDiffResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_commit_diff_with_options_async(repository_id, sha, request, headers, runtime)

    def list_repository_commits_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryCommitsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryCommitsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['path'] = request.path
        if not UtilClient.is_unset(request.ref_name):
            query['refName'] = request.ref_name
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.show_comments_count):
            query['showCommentsCount'] = request.show_comments_count
        if not UtilClient.is_unset(request.show_signature):
            query['showSignature'] = request.show_signature
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryCommits',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/commits',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryCommitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repository_commits_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryCommitsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryCommitsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['path'] = request.path
        if not UtilClient.is_unset(request.ref_name):
            query['refName'] = request.ref_name
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.show_comments_count):
            query['showCommentsCount'] = request.show_comments_count
        if not UtilClient.is_unset(request.show_signature):
            query['showSignature'] = request.show_signature
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryCommits',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/commits',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryCommitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repository_commits(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryCommitsRequest,
    ) -> devops_20210625_models.ListRepositoryCommitsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_commits_with_options(repository_id, request, headers, runtime)

    async def list_repository_commits_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryCommitsRequest,
    ) -> devops_20210625_models.ListRepositoryCommitsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_commits_with_options_async(repository_id, request, headers, runtime)

    def list_repository_groups_with_options(
        self,
        request: devops_20210625_models.ListRepositoryGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.include_personal):
            query['includePersonal'] = request.include_personal
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_id):
            query['parentId'] = request.parent_id
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/groups/get/all',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repository_groups_with_options_async(
        self,
        request: devops_20210625_models.ListRepositoryGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.include_personal):
            query['includePersonal'] = request.include_personal
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_id):
            query['parentId'] = request.parent_id
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/groups/get/all',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repository_groups(
        self,
        request: devops_20210625_models.ListRepositoryGroupsRequest,
    ) -> devops_20210625_models.ListRepositoryGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_groups_with_options(request, headers, runtime)

    async def list_repository_groups_async(
        self,
        request: devops_20210625_models.ListRepositoryGroupsRequest,
    ) -> devops_20210625_models.ListRepositoryGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_groups_with_options_async(request, headers, runtime)

    def list_repository_member_with_inherited_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryMemberWithInheritedRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryMemberWithInheritedResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryMemberWithInherited',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/members/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryMemberWithInheritedResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repository_member_with_inherited_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryMemberWithInheritedRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryMemberWithInheritedResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryMemberWithInherited',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/members/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryMemberWithInheritedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repository_member_with_inherited(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryMemberWithInheritedRequest,
    ) -> devops_20210625_models.ListRepositoryMemberWithInheritedResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_member_with_inherited_with_options(repository_id, request, headers, runtime)

    async def list_repository_member_with_inherited_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryMemberWithInheritedRequest,
    ) -> devops_20210625_models.ListRepositoryMemberWithInheritedResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_member_with_inherited_with_options_async(repository_id, request, headers, runtime)

    def list_repository_tags_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryTags',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/tag/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repository_tags_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryTags',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/tag/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repository_tags(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryTagsRequest,
    ) -> devops_20210625_models.ListRepositoryTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_tags_with_options(repository_id, request, headers, runtime)

    async def list_repository_tags_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryTagsRequest,
    ) -> devops_20210625_models.ListRepositoryTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_tags_with_options_async(repository_id, request, headers, runtime)

    def list_repository_tree_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryTreeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryTreeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.path):
            query['path'] = request.path
        if not UtilClient.is_unset(request.ref_name):
            query['refName'] = request.ref_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryTree',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files/tree',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repository_tree_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryTreeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryTreeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.path):
            query['path'] = request.path
        if not UtilClient.is_unset(request.ref_name):
            query['refName'] = request.ref_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryTree',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files/tree',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repository_tree(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryTreeRequest,
    ) -> devops_20210625_models.ListRepositoryTreeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_tree_with_options(repository_id, request, headers, runtime)

    async def list_repository_tree_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryTreeRequest,
    ) -> devops_20210625_models.ListRepositoryTreeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_tree_with_options_async(repository_id, request, headers, runtime)

    def list_repository_webhook_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryWebhook',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/webhooks/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repository_webhook_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryWebhook',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/webhooks/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repository_webhook(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryWebhookRequest,
    ) -> devops_20210625_models.ListRepositoryWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_webhook_with_options(repository_id, request, headers, runtime)

    async def list_repository_webhook_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryWebhookRequest,
    ) -> devops_20210625_models.ListRepositoryWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_webhook_with_options_async(repository_id, request, headers, runtime)

    def list_resource_members_with_options(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListResourceMembersResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListResourceMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(resource_type)}/{OpenApiUtilClient.get_encode_param(resource_id)}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListResourceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_members_with_options_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListResourceMembersResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListResourceMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(resource_type)}/{OpenApiUtilClient.get_encode_param(resource_id)}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListResourceMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_members(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
    ) -> devops_20210625_models.ListResourceMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_members_with_options(organization_id, resource_type, resource_id, headers, runtime)

    async def list_resource_members_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
    ) -> devops_20210625_models.ListResourceMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_members_with_options_async(organization_id, resource_type, resource_id, headers, runtime)

    def list_search_commit_with_options(
        self,
        request: devops_20210625_models.ListSearchCommitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListSearchCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.keyword):
            body['keyword'] = request.keyword
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.page):
            body['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_path):
            body['repoPath'] = request.repo_path
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.sort):
            body['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSearchCommit',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/search/commit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListSearchCommitResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_search_commit_with_options_async(
        self,
        request: devops_20210625_models.ListSearchCommitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListSearchCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.keyword):
            body['keyword'] = request.keyword
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.page):
            body['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_path):
            body['repoPath'] = request.repo_path
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.sort):
            body['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSearchCommit',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/search/commit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListSearchCommitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_search_commit(
        self,
        request: devops_20210625_models.ListSearchCommitRequest,
    ) -> devops_20210625_models.ListSearchCommitResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_search_commit_with_options(request, headers, runtime)

    async def list_search_commit_async(
        self,
        request: devops_20210625_models.ListSearchCommitRequest,
    ) -> devops_20210625_models.ListSearchCommitResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_search_commit_with_options_async(request, headers, runtime)

    def list_search_repository_with_options(
        self,
        request: devops_20210625_models.ListSearchRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListSearchRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.aliyun_pk):
            body['aliyunPk'] = request.aliyun_pk
        if not UtilClient.is_unset(request.keyword):
            body['keyword'] = request.keyword
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.page):
            body['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_path):
            body['repoPath'] = request.repo_path
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.sort):
            body['sort'] = request.sort
        if not UtilClient.is_unset(request.visibility_level):
            body['visibilityLevel'] = request.visibility_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSearchRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/search/repo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListSearchRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_search_repository_with_options_async(
        self,
        request: devops_20210625_models.ListSearchRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListSearchRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.aliyun_pk):
            body['aliyunPk'] = request.aliyun_pk
        if not UtilClient.is_unset(request.keyword):
            body['keyword'] = request.keyword
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.page):
            body['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_path):
            body['repoPath'] = request.repo_path
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.sort):
            body['sort'] = request.sort
        if not UtilClient.is_unset(request.visibility_level):
            body['visibilityLevel'] = request.visibility_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSearchRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/search/repo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListSearchRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_search_repository(
        self,
        request: devops_20210625_models.ListSearchRepositoryRequest,
    ) -> devops_20210625_models.ListSearchRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_search_repository_with_options(request, headers, runtime)

    async def list_search_repository_async(
        self,
        request: devops_20210625_models.ListSearchRepositoryRequest,
    ) -> devops_20210625_models.ListSearchRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_search_repository_with_options_async(request, headers, runtime)

    def list_search_source_code_with_options(
        self,
        request: devops_20210625_models.ListSearchSourceCodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListSearchSourceCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        if not UtilClient.is_unset(request.is_code_block):
            body['isCodeBlock'] = request.is_code_block
        if not UtilClient.is_unset(request.keyword):
            body['keyword'] = request.keyword
        if not UtilClient.is_unset(request.language):
            body['language'] = request.language
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.page):
            body['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_path):
            body['repoPath'] = request.repo_path
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.sort):
            body['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSearchSourceCode',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/search/code',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListSearchSourceCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_search_source_code_with_options_async(
        self,
        request: devops_20210625_models.ListSearchSourceCodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListSearchSourceCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        if not UtilClient.is_unset(request.is_code_block):
            body['isCodeBlock'] = request.is_code_block
        if not UtilClient.is_unset(request.keyword):
            body['keyword'] = request.keyword
        if not UtilClient.is_unset(request.language):
            body['language'] = request.language
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.page):
            body['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_path):
            body['repoPath'] = request.repo_path
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.sort):
            body['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSearchSourceCode',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/search/code',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListSearchSourceCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_search_source_code(
        self,
        request: devops_20210625_models.ListSearchSourceCodeRequest,
    ) -> devops_20210625_models.ListSearchSourceCodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_search_source_code_with_options(request, headers, runtime)

    async def list_search_source_code_async(
        self,
        request: devops_20210625_models.ListSearchSourceCodeRequest,
    ) -> devops_20210625_models.ListSearchSourceCodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_search_source_code_with_options_async(request, headers, runtime)

    def list_service_auths_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListServiceAuthsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListServiceAuthsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_auth_type):
            query['serviceAuthType'] = request.service_auth_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceAuths',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/serviceAuths',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListServiceAuthsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_auths_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListServiceAuthsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListServiceAuthsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_auth_type):
            query['serviceAuthType'] = request.service_auth_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceAuths',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/serviceAuths',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListServiceAuthsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_auths(
        self,
        organization_id: str,
        request: devops_20210625_models.ListServiceAuthsRequest,
    ) -> devops_20210625_models.ListServiceAuthsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_auths_with_options(organization_id, request, headers, runtime)

    async def list_service_auths_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListServiceAuthsRequest,
    ) -> devops_20210625_models.ListServiceAuthsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_service_auths_with_options_async(organization_id, request, headers, runtime)

    def list_service_connections_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListServiceConnectionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListServiceConnectionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.serice_connection_type):
            query['sericeConnectionType'] = request.serice_connection_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceConnections',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/serviceConnections',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListServiceConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_connections_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListServiceConnectionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListServiceConnectionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.serice_connection_type):
            query['sericeConnectionType'] = request.serice_connection_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceConnections',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/serviceConnections',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListServiceConnectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_connections(
        self,
        organization_id: str,
        request: devops_20210625_models.ListServiceConnectionsRequest,
    ) -> devops_20210625_models.ListServiceConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_connections_with_options(organization_id, request, headers, runtime)

    async def list_service_connections_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListServiceConnectionsRequest,
    ) -> devops_20210625_models.ListServiceConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_service_connections_with_options_async(organization_id, request, headers, runtime)

    def list_service_credentials_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListServiceCredentialsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListServiceCredentialsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_credential_type):
            query['serviceCredentialType'] = request.service_credential_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceCredentials',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/serviceCredentials',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListServiceCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_credentials_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListServiceCredentialsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListServiceCredentialsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_credential_type):
            query['serviceCredentialType'] = request.service_credential_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceCredentials',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/serviceCredentials',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListServiceCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_credentials(
        self,
        organization_id: str,
        request: devops_20210625_models.ListServiceCredentialsRequest,
    ) -> devops_20210625_models.ListServiceCredentialsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_credentials_with_options(organization_id, request, headers, runtime)

    async def list_service_credentials_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListServiceCredentialsRequest,
    ) -> devops_20210625_models.ListServiceCredentialsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_service_credentials_with_options_async(organization_id, request, headers, runtime)

    def list_sprints_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListSprintsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListSprintsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSprints',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/sprints/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListSprintsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sprints_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListSprintsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListSprintsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSprints',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/sprints/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListSprintsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sprints(
        self,
        organization_id: str,
        request: devops_20210625_models.ListSprintsRequest,
    ) -> devops_20210625_models.ListSprintsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_sprints_with_options(organization_id, request, headers, runtime)

    async def list_sprints_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListSprintsRequest,
    ) -> devops_20210625_models.ListSprintsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_sprints_with_options_async(organization_id, request, headers, runtime)

    def list_test_case_fields_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListTestCaseFieldsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListTestCaseFieldsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTestCaseFields',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/testhub/testcase/fields',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListTestCaseFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_test_case_fields_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListTestCaseFieldsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListTestCaseFieldsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTestCaseFields',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/testhub/testcase/fields',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListTestCaseFieldsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_test_case_fields(
        self,
        organization_id: str,
        request: devops_20210625_models.ListTestCaseFieldsRequest,
    ) -> devops_20210625_models.ListTestCaseFieldsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_test_case_fields_with_options(organization_id, request, headers, runtime)

    async def list_test_case_fields_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListTestCaseFieldsRequest,
    ) -> devops_20210625_models.ListTestCaseFieldsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_test_case_fields_with_options_async(organization_id, request, headers, runtime)

    def list_user_draw_record_by_pk_with_options(
        self,
        request: devops_20210625_models.ListUserDrawRecordByPkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListUserDrawRecordByPkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_pk):
            query['aliyunPk'] = request.aliyun_pk
        if not UtilClient.is_unset(request.draw_group):
            query['drawGroup'] = request.draw_group
        if not UtilClient.is_unset(request.draw_pool_name):
            query['drawPoolName'] = request.draw_pool_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserDrawRecordByPk',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/listUserDrawRecords',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListUserDrawRecordByPkResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_draw_record_by_pk_with_options_async(
        self,
        request: devops_20210625_models.ListUserDrawRecordByPkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListUserDrawRecordByPkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_pk):
            query['aliyunPk'] = request.aliyun_pk
        if not UtilClient.is_unset(request.draw_group):
            query['drawGroup'] = request.draw_group
        if not UtilClient.is_unset(request.draw_pool_name):
            query['drawPoolName'] = request.draw_pool_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserDrawRecordByPk',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/listUserDrawRecords',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListUserDrawRecordByPkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_draw_record_by_pk(
        self,
        request: devops_20210625_models.ListUserDrawRecordByPkRequest,
    ) -> devops_20210625_models.ListUserDrawRecordByPkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_draw_record_by_pk_with_options(request, headers, runtime)

    async def list_user_draw_record_by_pk_async(
        self,
        request: devops_20210625_models.ListUserDrawRecordByPkRequest,
    ) -> devops_20210625_models.ListUserDrawRecordByPkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_user_draw_record_by_pk_with_options_async(request, headers, runtime)

    def list_user_keys_with_options(
        self,
        request: devops_20210625_models.ListUserKeysRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListUserKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserKeys',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v3/user/keys',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListUserKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_keys_with_options_async(
        self,
        request: devops_20210625_models.ListUserKeysRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListUserKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserKeys',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v3/user/keys',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListUserKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_keys(
        self,
        request: devops_20210625_models.ListUserKeysRequest,
    ) -> devops_20210625_models.ListUserKeysResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_keys_with_options(request, headers, runtime)

    async def list_user_keys_async(
        self,
        request: devops_20210625_models.ListUserKeysRequest,
    ) -> devops_20210625_models.ListUserKeysResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_user_keys_with_options_async(request, headers, runtime)

    def list_user_resources_with_options(
        self,
        request: devops_20210625_models.ListUserResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListUserResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_ids):
            query['userIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserResources',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/user/vision/user_resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListUserResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_resources_with_options_async(
        self,
        request: devops_20210625_models.ListUserResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListUserResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_ids):
            query['userIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserResources',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/user/vision/user_resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListUserResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_resources(
        self,
        request: devops_20210625_models.ListUserResourcesRequest,
    ) -> devops_20210625_models.ListUserResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_resources_with_options(request, headers, runtime)

    async def list_user_resources_async(
        self,
        request: devops_20210625_models.ListUserResourcesRequest,
    ) -> devops_20210625_models.ListUserResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_user_resources_with_options_async(request, headers, runtime)

    def list_variable_groups_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListVariableGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListVariableGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_order):
            query['pageOrder'] = request.page_order
        if not UtilClient.is_unset(request.page_sort):
            query['pageSort'] = request.page_sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVariableGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/variableGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListVariableGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_variable_groups_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListVariableGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListVariableGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_order):
            query['pageOrder'] = request.page_order
        if not UtilClient.is_unset(request.page_sort):
            query['pageSort'] = request.page_sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVariableGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/variableGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListVariableGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_variable_groups(
        self,
        organization_id: str,
        request: devops_20210625_models.ListVariableGroupsRequest,
    ) -> devops_20210625_models.ListVariableGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_variable_groups_with_options(organization_id, request, headers, runtime)

    async def list_variable_groups_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListVariableGroupsRequest,
    ) -> devops_20210625_models.ListVariableGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_variable_groups_with_options_async(organization_id, request, headers, runtime)

    def list_work_item_all_fields_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkItemAllFieldsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkItemAllFieldsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        if not UtilClient.is_unset(request.workitem_type_identifier):
            query['workitemTypeIdentifier'] = request.workitem_type_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkItemAllFields',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/fields/listAll',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkItemAllFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_work_item_all_fields_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkItemAllFieldsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkItemAllFieldsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        if not UtilClient.is_unset(request.workitem_type_identifier):
            query['workitemTypeIdentifier'] = request.workitem_type_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkItemAllFields',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/fields/listAll',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkItemAllFieldsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_work_item_all_fields(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkItemAllFieldsRequest,
    ) -> devops_20210625_models.ListWorkItemAllFieldsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_work_item_all_fields_with_options(organization_id, request, headers, runtime)

    async def list_work_item_all_fields_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkItemAllFieldsRequest,
    ) -> devops_20210625_models.ListWorkItemAllFieldsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_work_item_all_fields_with_options_async(organization_id, request, headers, runtime)

    def list_work_item_work_flow_status_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkItemWorkFlowStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkItemWorkFlowStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        if not UtilClient.is_unset(request.workitem_category_identifier):
            query['workitemCategoryIdentifier'] = request.workitem_category_identifier
        if not UtilClient.is_unset(request.workitem_type_identifier):
            query['workitemTypeIdentifier'] = request.workitem_type_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkItemWorkFlowStatus',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/workflow/listWorkflowStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkItemWorkFlowStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_work_item_work_flow_status_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkItemWorkFlowStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkItemWorkFlowStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        if not UtilClient.is_unset(request.workitem_category_identifier):
            query['workitemCategoryIdentifier'] = request.workitem_category_identifier
        if not UtilClient.is_unset(request.workitem_type_identifier):
            query['workitemTypeIdentifier'] = request.workitem_type_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkItemWorkFlowStatus',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/workflow/listWorkflowStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkItemWorkFlowStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_work_item_work_flow_status(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkItemWorkFlowStatusRequest,
    ) -> devops_20210625_models.ListWorkItemWorkFlowStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_work_item_work_flow_status_with_options(organization_id, request, headers, runtime)

    async def list_work_item_work_flow_status_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkItemWorkFlowStatusRequest,
    ) -> devops_20210625_models.ListWorkItemWorkFlowStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_work_item_work_flow_status_with_options_async(organization_id, request, headers, runtime)

    def list_workitem_attachments_with_options(
        self,
        organization_id: str,
        workitem_identifier: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkitemAttachmentsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListWorkitemAttachments',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitem/{OpenApiUtilClient.get_encode_param(workitem_identifier)}/attachments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkitemAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workitem_attachments_with_options_async(
        self,
        organization_id: str,
        workitem_identifier: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkitemAttachmentsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListWorkitemAttachments',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitem/{OpenApiUtilClient.get_encode_param(workitem_identifier)}/attachments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkitemAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workitem_attachments(
        self,
        organization_id: str,
        workitem_identifier: str,
    ) -> devops_20210625_models.ListWorkitemAttachmentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workitem_attachments_with_options(organization_id, workitem_identifier, headers, runtime)

    async def list_workitem_attachments_async(
        self,
        organization_id: str,
        workitem_identifier: str,
    ) -> devops_20210625_models.ListWorkitemAttachmentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workitem_attachments_with_options_async(organization_id, workitem_identifier, headers, runtime)

    def list_workitem_estimate_with_options(
        self,
        organization_id: str,
        workitem_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkitemEstimateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListWorkitemEstimate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/estimate/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkitemEstimateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workitem_estimate_with_options_async(
        self,
        organization_id: str,
        workitem_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkitemEstimateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListWorkitemEstimate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/estimate/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkitemEstimateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workitem_estimate(
        self,
        organization_id: str,
        workitem_id: str,
    ) -> devops_20210625_models.ListWorkitemEstimateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workitem_estimate_with_options(organization_id, workitem_id, headers, runtime)

    async def list_workitem_estimate_async(
        self,
        organization_id: str,
        workitem_id: str,
    ) -> devops_20210625_models.ListWorkitemEstimateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workitem_estimate_with_options_async(organization_id, workitem_id, headers, runtime)

    def list_workitem_time_with_options(
        self,
        organization_id: str,
        workitem_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkitemTimeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListWorkitemTime',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/time/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkitemTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workitem_time_with_options_async(
        self,
        organization_id: str,
        workitem_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkitemTimeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListWorkitemTime',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/time/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkitemTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workitem_time(
        self,
        organization_id: str,
        workitem_id: str,
    ) -> devops_20210625_models.ListWorkitemTimeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workitem_time_with_options(organization_id, workitem_id, headers, runtime)

    async def list_workitem_time_async(
        self,
        organization_id: str,
        workitem_id: str,
    ) -> devops_20210625_models.ListWorkitemTimeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workitem_time_with_options_async(organization_id, workitem_id, headers, runtime)

    def list_workitems_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkitemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkitemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.conditions):
            query['conditions'] = request.conditions
        if not UtilClient.is_unset(request.extra_conditions):
            query['extraConditions'] = request.extra_conditions
        if not UtilClient.is_unset(request.group_condition):
            query['groupCondition'] = request.group_condition
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.search_type):
            query['searchType'] = request.search_type
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkitems',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/listWorkitems',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkitemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workitems_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkitemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkitemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.conditions):
            query['conditions'] = request.conditions
        if not UtilClient.is_unset(request.extra_conditions):
            query['extraConditions'] = request.extra_conditions
        if not UtilClient.is_unset(request.group_condition):
            query['groupCondition'] = request.group_condition
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.search_type):
            query['searchType'] = request.search_type
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkitems',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/listWorkitems',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkitemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workitems(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkitemsRequest,
    ) -> devops_20210625_models.ListWorkitemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workitems_with_options(organization_id, request, headers, runtime)

    async def list_workitems_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkitemsRequest,
    ) -> devops_20210625_models.ListWorkitemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workitems_with_options_async(organization_id, request, headers, runtime)

    def list_workspaces_with_options(
        self,
        tmp_req: devops_20210625_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkspacesResponse:
        UtilClient.validate_model(tmp_req)
        request = devops_20210625_models.ListWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.status_list):
            request.status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status_list, 'statusList', 'simple')
        if not UtilClient.is_unset(tmp_req.workspace_template_list):
            request.workspace_template_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workspace_template_list, 'workspaceTemplateList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.status_list_shrink):
            query['statusList'] = request.status_list_shrink
        if not UtilClient.is_unset(request.workspace_template_list_shrink):
            query['workspaceTemplateList'] = request.workspace_template_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspaces_with_options_async(
        self,
        tmp_req: devops_20210625_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkspacesResponse:
        UtilClient.validate_model(tmp_req)
        request = devops_20210625_models.ListWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.status_list):
            request.status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status_list, 'statusList', 'simple')
        if not UtilClient.is_unset(tmp_req.workspace_template_list):
            request.workspace_template_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workspace_template_list, 'workspaceTemplateList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.status_list_shrink):
            query['statusList'] = request.status_list_shrink
        if not UtilClient.is_unset(request.workspace_template_list_shrink):
            query['workspaceTemplateList'] = request.workspace_template_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkspacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspaces(
        self,
        request: devops_20210625_models.ListWorkspacesRequest,
    ) -> devops_20210625_models.ListWorkspacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workspaces_with_options(request, headers, runtime)

    async def list_workspaces_async(
        self,
        request: devops_20210625_models.ListWorkspacesRequest,
    ) -> devops_20210625_models.ListWorkspacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workspaces_with_options_async(request, headers, runtime)

    def log_pipeline_job_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        job_id: str,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.LogPipelineJobRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='LogPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRun/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/job/{OpenApiUtilClient.get_encode_param(job_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.LogPipelineJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def log_pipeline_job_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        job_id: str,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.LogPipelineJobRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='LogPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRun/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/job/{OpenApiUtilClient.get_encode_param(job_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.LogPipelineJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def log_pipeline_job_run(
        self,
        organization_id: str,
        pipeline_id: str,
        job_id: str,
        pipeline_run_id: str,
    ) -> devops_20210625_models.LogPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.log_pipeline_job_run_with_options(organization_id, pipeline_id, job_id, pipeline_run_id, headers, runtime)

    async def log_pipeline_job_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        job_id: str,
        pipeline_run_id: str,
    ) -> devops_20210625_models.LogPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.log_pipeline_job_run_with_options_async(organization_id, pipeline_id, job_id, pipeline_run_id, headers, runtime)

    def log_vmdeploy_machine_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.LogVMDeployMachineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='LogVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}/machine/{OpenApiUtilClient.get_encode_param(machine_sn)}/log',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.LogVMDeployMachineResponse(),
            self.call_api(params, req, runtime)
        )

    async def log_vmdeploy_machine_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.LogVMDeployMachineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='LogVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}/machine/{OpenApiUtilClient.get_encode_param(machine_sn)}/log',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.LogVMDeployMachineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def log_vmdeploy_machine(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
    ) -> devops_20210625_models.LogVMDeployMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.log_vmdeploy_machine_with_options(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    async def log_vmdeploy_machine_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
    ) -> devops_20210625_models.LogVMDeployMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.log_vmdeploy_machine_with_options_async(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    def merge_merge_request_with_options(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.MergeMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.MergeMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.merge_message):
            body['mergeMessage'] = request.merge_message
        if not UtilClient.is_unset(request.merge_type):
            body['mergeType'] = request.merge_type
        if not UtilClient.is_unset(request.remove_source_branch):
            body['removeSourceBranch'] = request.remove_source_branch
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MergeMergeRequest',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/merge_requests/{OpenApiUtilClient.get_encode_param(local_id)}/merge',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.MergeMergeRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def merge_merge_request_with_options_async(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.MergeMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.MergeMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.merge_message):
            body['mergeMessage'] = request.merge_message
        if not UtilClient.is_unset(request.merge_type):
            body['mergeType'] = request.merge_type
        if not UtilClient.is_unset(request.remove_source_branch):
            body['removeSourceBranch'] = request.remove_source_branch
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MergeMergeRequest',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/merge_requests/{OpenApiUtilClient.get_encode_param(local_id)}/merge',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.MergeMergeRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def merge_merge_request(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.MergeMergeRequestRequest,
    ) -> devops_20210625_models.MergeMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.merge_merge_request_with_options(repository_id, local_id, request, headers, runtime)

    async def merge_merge_request_async(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.MergeMergeRequestRequest,
    ) -> devops_20210625_models.MergeMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.merge_merge_request_with_options_async(repository_id, local_id, request, headers, runtime)

    def pass_pipeline_validate_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.PassPipelineValidateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PassPipelineValidate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/pass',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.PassPipelineValidateResponse(),
            self.call_api(params, req, runtime)
        )

    async def pass_pipeline_validate_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.PassPipelineValidateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PassPipelineValidate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/pass',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.PassPipelineValidateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pass_pipeline_validate(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.PassPipelineValidateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pass_pipeline_validate_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    async def pass_pipeline_validate_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.PassPipelineValidateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.pass_pipeline_validate_with_options_async(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def refuse_pipeline_validate_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.RefusePipelineValidateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RefusePipelineValidate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/refuse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RefusePipelineValidateResponse(),
            self.call_api(params, req, runtime)
        )

    async def refuse_pipeline_validate_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.RefusePipelineValidateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RefusePipelineValidate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/refuse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RefusePipelineValidateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refuse_pipeline_validate(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.RefusePipelineValidateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.refuse_pipeline_validate_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    async def refuse_pipeline_validate_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.RefusePipelineValidateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.refuse_pipeline_validate_with_options_async(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def release_workspace_with_options(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ReleaseWorkspaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ReleaseWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/release',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ReleaseWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_workspace_with_options_async(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ReleaseWorkspaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ReleaseWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/release',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ReleaseWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_workspace(
        self,
        workspace_id: str,
    ) -> devops_20210625_models.ReleaseWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.release_workspace_with_options(workspace_id, headers, runtime)

    async def release_workspace_async(
        self,
        workspace_id: str,
    ) -> devops_20210625_models.ReleaseWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.release_workspace_with_options_async(workspace_id, headers, runtime)

    def reopen_merge_request_with_options(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.ReopenMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ReopenMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReopenMergeRequest',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/merge_requests/{OpenApiUtilClient.get_encode_param(local_id)}/reopen',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ReopenMergeRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def reopen_merge_request_with_options_async(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.ReopenMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ReopenMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReopenMergeRequest',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/merge_requests/{OpenApiUtilClient.get_encode_param(local_id)}/reopen',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ReopenMergeRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reopen_merge_request(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.ReopenMergeRequestRequest,
    ) -> devops_20210625_models.ReopenMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reopen_merge_request_with_options(repository_id, local_id, request, headers, runtime)

    async def reopen_merge_request_async(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.ReopenMergeRequestRequest,
    ) -> devops_20210625_models.ReopenMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.reopen_merge_request_with_options_async(repository_id, local_id, request, headers, runtime)

    def reset_ssh_key_with_options(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ResetSshKeyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResetSshKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/sshKey',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ResetSshKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_ssh_key_with_options_async(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ResetSshKeyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResetSshKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/sshKey',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ResetSshKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_ssh_key(
        self,
        organization_id: str,
    ) -> devops_20210625_models.ResetSshKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reset_ssh_key_with_options(organization_id, headers, runtime)

    async def reset_ssh_key_async(
        self,
        organization_id: str,
    ) -> devops_20210625_models.ResetSshKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.reset_ssh_key_with_options_async(organization_id, headers, runtime)

    def resume_vmdeploy_order_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ResumeVMDeployOrderResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}/resume',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ResumeVMDeployOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_vmdeploy_order_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ResumeVMDeployOrderResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}/resume',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ResumeVMDeployOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_vmdeploy_order(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
    ) -> devops_20210625_models.ResumeVMDeployOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_vmdeploy_order_with_options(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    async def resume_vmdeploy_order_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
    ) -> devops_20210625_models.ResumeVMDeployOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.resume_vmdeploy_order_with_options_async(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    def retry_pipeline_job_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.RetryPipelineJobRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RetryPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RetryPipelineJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_pipeline_job_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.RetryPipelineJobRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RetryPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RetryPipelineJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_pipeline_job_run(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.RetryPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.retry_pipeline_job_run_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    async def retry_pipeline_job_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.RetryPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.retry_pipeline_job_run_with_options_async(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def retry_vmdeploy_machine_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.RetryVMDeployMachineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RetryVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}/machine/{OpenApiUtilClient.get_encode_param(machine_sn)}/retry',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RetryVMDeployMachineResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_vmdeploy_machine_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.RetryVMDeployMachineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RetryVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}/machine/{OpenApiUtilClient.get_encode_param(machine_sn)}/retry',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RetryVMDeployMachineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_vmdeploy_machine(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
    ) -> devops_20210625_models.RetryVMDeployMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.retry_vmdeploy_machine_with_options(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    async def retry_vmdeploy_machine_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
    ) -> devops_20210625_models.RetryVMDeployMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.retry_vmdeploy_machine_with_options_async(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    def review_merge_request_with_options(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.ReviewMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ReviewMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.draft_comment_ids):
            body['draftCommentIds'] = request.draft_comment_ids
        if not UtilClient.is_unset(request.review_comment):
            body['reviewComment'] = request.review_comment
        if not UtilClient.is_unset(request.review_opinion):
            body['reviewOpinion'] = request.review_opinion
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReviewMergeRequest',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/merge_requests/{OpenApiUtilClient.get_encode_param(local_id)}/submit_review_opinion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ReviewMergeRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def review_merge_request_with_options_async(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.ReviewMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ReviewMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.draft_comment_ids):
            body['draftCommentIds'] = request.draft_comment_ids
        if not UtilClient.is_unset(request.review_comment):
            body['reviewComment'] = request.review_comment
        if not UtilClient.is_unset(request.review_opinion):
            body['reviewOpinion'] = request.review_opinion
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReviewMergeRequest',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/merge_requests/{OpenApiUtilClient.get_encode_param(local_id)}/submit_review_opinion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ReviewMergeRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def review_merge_request(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.ReviewMergeRequestRequest,
    ) -> devops_20210625_models.ReviewMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.review_merge_request_with_options(repository_id, local_id, request, headers, runtime)

    async def review_merge_request_async(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.ReviewMergeRequestRequest,
    ) -> devops_20210625_models.ReviewMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.review_merge_request_with_options_async(repository_id, local_id, request, headers, runtime)

    def skip_pipeline_job_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.SkipPipelineJobRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SkipPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/skip',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.SkipPipelineJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def skip_pipeline_job_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.SkipPipelineJobRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SkipPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/skip',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.SkipPipelineJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def skip_pipeline_job_run(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.SkipPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.skip_pipeline_job_run_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    async def skip_pipeline_job_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.SkipPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.skip_pipeline_job_run_with_options_async(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def skip_vmdeploy_machine_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.SkipVMDeployMachineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SkipVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}/machine/{OpenApiUtilClient.get_encode_param(machine_sn)}/skip',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.SkipVMDeployMachineResponse(),
            self.call_api(params, req, runtime)
        )

    async def skip_vmdeploy_machine_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.SkipVMDeployMachineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SkipVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}/machine/{OpenApiUtilClient.get_encode_param(machine_sn)}/skip',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.SkipVMDeployMachineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def skip_vmdeploy_machine(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
    ) -> devops_20210625_models.SkipVMDeployMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.skip_vmdeploy_machine_with_options(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    async def skip_vmdeploy_machine_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
    ) -> devops_20210625_models.SkipVMDeployMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.skip_vmdeploy_machine_with_options_async(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    def start_pipeline_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.StartPipelineRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StartPipelineRunResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organizations/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/run',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StartPipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_pipeline_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.StartPipelineRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StartPipelineRunResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organizations/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/run',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StartPipelineRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_pipeline_run(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.StartPipelineRunRequest,
    ) -> devops_20210625_models.StartPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_pipeline_run_with_options(organization_id, pipeline_id, request, headers, runtime)

    async def start_pipeline_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.StartPipelineRunRequest,
    ) -> devops_20210625_models.StartPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_pipeline_run_with_options_async(organization_id, pipeline_id, request, headers, runtime)

    def stop_pipeline_job_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StopPipelineJobRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopPipelineJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_pipeline_job_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StopPipelineJobRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopPipelineJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_pipeline_job_run(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.StopPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_pipeline_job_run_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    async def stop_pipeline_job_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.StopPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_pipeline_job_run_with_options_async(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def stop_pipeline_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StopPipelineRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopPipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_pipeline_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StopPipelineRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopPipelineRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_pipeline_run(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
    ) -> devops_20210625_models.StopPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_pipeline_run_with_options(organization_id, pipeline_id, pipeline_run_id, headers, runtime)

    async def stop_pipeline_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
    ) -> devops_20210625_models.StopPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_pipeline_run_with_options_async(organization_id, pipeline_id, pipeline_run_id, headers, runtime)

    def stop_vmdeploy_order_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StopVMDeployOrderResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopVMDeployOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_vmdeploy_order_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StopVMDeployOrderResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopVMDeployOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_vmdeploy_order(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
    ) -> devops_20210625_models.StopVMDeployOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_vmdeploy_order_with_options(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    async def stop_vmdeploy_order_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
    ) -> devops_20210625_models.StopVMDeployOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_vmdeploy_order_with_options_async(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    def transfer_repository_with_options(
        self,
        request: devops_20210625_models.TransferRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.TransferRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_id):
            query['repositoryId'] = request.repository_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/repository/transfer',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.TransferRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_repository_with_options_async(
        self,
        request: devops_20210625_models.TransferRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.TransferRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_id):
            query['repositoryId'] = request.repository_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/repository/transfer',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.TransferRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_repository(
        self,
        request: devops_20210625_models.TransferRepositoryRequest,
    ) -> devops_20210625_models.TransferRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.transfer_repository_with_options(request, headers, runtime)

    async def transfer_repository_async(
        self,
        request: devops_20210625_models.TransferRepositoryRequest,
    ) -> devops_20210625_models.TransferRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.transfer_repository_with_options_async(request, headers, runtime)

    def trigger_repository_mirror_sync_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.TriggerRepositoryMirrorSyncRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.TriggerRepositoryMirrorSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.account):
            query['account'] = request.account
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerRepositoryMirrorSync',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/mirror',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.TriggerRepositoryMirrorSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_repository_mirror_sync_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.TriggerRepositoryMirrorSyncRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.TriggerRepositoryMirrorSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.account):
            query['account'] = request.account
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerRepositoryMirrorSync',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/mirror',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.TriggerRepositoryMirrorSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_repository_mirror_sync(
        self,
        repository_id: str,
        request: devops_20210625_models.TriggerRepositoryMirrorSyncRequest,
    ) -> devops_20210625_models.TriggerRepositoryMirrorSyncResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.trigger_repository_mirror_sync_with_options(repository_id, request, headers, runtime)

    async def trigger_repository_mirror_sync_async(
        self,
        repository_id: str,
        request: devops_20210625_models.TriggerRepositoryMirrorSyncRequest,
    ) -> devops_20210625_models.TriggerRepositoryMirrorSyncResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.trigger_repository_mirror_sync_with_options_async(repository_id, request, headers, runtime)

    def update_app_member_with_options(
        self,
        app_name: str,
        request: devops_20210625_models.UpdateAppMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateAppMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.player):
            body['player'] = request.player
        if not UtilClient.is_unset(request.role_names):
            body['roleNames'] = request.role_names
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAppMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/appstack/apps/{OpenApiUtilClient.get_encode_param(app_name)}/members',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateAppMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_member_with_options_async(
        self,
        app_name: str,
        request: devops_20210625_models.UpdateAppMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateAppMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.player):
            body['player'] = request.player
        if not UtilClient.is_unset(request.role_names):
            body['roleNames'] = request.role_names
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAppMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/appstack/apps/{OpenApiUtilClient.get_encode_param(app_name)}/members',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateAppMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_member(
        self,
        app_name: str,
        request: devops_20210625_models.UpdateAppMemberRequest,
    ) -> devops_20210625_models.UpdateAppMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_app_member_with_options(app_name, request, headers, runtime)

    async def update_app_member_async(
        self,
        app_name: str,
        request: devops_20210625_models.UpdateAppMemberRequest,
    ) -> devops_20210625_models.UpdateAppMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_app_member_with_options_async(app_name, request, headers, runtime)

    def update_application_with_options(
        self,
        app_name: str,
        request: devops_20210625_models.UpdateApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.owner_account_id):
            body['ownerAccountId'] = request.owner_account_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateApplication',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/appstack/apps/{OpenApiUtilClient.get_encode_param(app_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_with_options_async(
        self,
        app_name: str,
        request: devops_20210625_models.UpdateApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.owner_account_id):
            body['ownerAccountId'] = request.owner_account_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateApplication',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/appstack/apps/{OpenApiUtilClient.get_encode_param(app_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application(
        self,
        app_name: str,
        request: devops_20210625_models.UpdateApplicationRequest,
    ) -> devops_20210625_models.UpdateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_application_with_options(app_name, request, headers, runtime)

    async def update_application_async(
        self,
        app_name: str,
        request: devops_20210625_models.UpdateApplicationRequest,
    ) -> devops_20210625_models.UpdateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_application_with_options_async(app_name, request, headers, runtime)

    def update_check_run_with_options(
        self,
        request: devops_20210625_models.UpdateCheckRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateCheckRunResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.check_run_id):
            query['checkRunId'] = request.check_run_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        body = {}
        if not UtilClient.is_unset(request.annotations):
            body['annotations'] = request.annotations
        if not UtilClient.is_unset(request.completed_at):
            body['completedAt'] = request.completed_at
        if not UtilClient.is_unset(request.conclusion):
            body['conclusion'] = request.conclusion
        if not UtilClient.is_unset(request.details_url):
            body['detailsUrl'] = request.details_url
        if not UtilClient.is_unset(request.external_id):
            body['externalId'] = request.external_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.output):
            body['output'] = request.output
        if not UtilClient.is_unset(request.started_at):
            body['startedAt'] = request.started_at
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCheckRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/check_runs/update_check_run',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateCheckRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_check_run_with_options_async(
        self,
        request: devops_20210625_models.UpdateCheckRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateCheckRunResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.check_run_id):
            query['checkRunId'] = request.check_run_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        body = {}
        if not UtilClient.is_unset(request.annotations):
            body['annotations'] = request.annotations
        if not UtilClient.is_unset(request.completed_at):
            body['completedAt'] = request.completed_at
        if not UtilClient.is_unset(request.conclusion):
            body['conclusion'] = request.conclusion
        if not UtilClient.is_unset(request.details_url):
            body['detailsUrl'] = request.details_url
        if not UtilClient.is_unset(request.external_id):
            body['externalId'] = request.external_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.output):
            body['output'] = request.output
        if not UtilClient.is_unset(request.started_at):
            body['startedAt'] = request.started_at
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCheckRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/check_runs/update_check_run',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateCheckRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_check_run(
        self,
        request: devops_20210625_models.UpdateCheckRunRequest,
    ) -> devops_20210625_models.UpdateCheckRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_check_run_with_options(request, headers, runtime)

    async def update_check_run_async(
        self,
        request: devops_20210625_models.UpdateCheckRunRequest,
    ) -> devops_20210625_models.UpdateCheckRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_check_run_with_options_async(request, headers, runtime)

    def update_file_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.UpdateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.branch_name):
            body['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.commit_message):
            body['commitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.encoding):
            body['encoding'] = request.encoding
        if not UtilClient.is_unset(request.new_path):
            body['newPath'] = request.new_path
        if not UtilClient.is_unset(request.old_path):
            body['oldPath'] = request.old_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFile',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files/update',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_file_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.UpdateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.branch_name):
            body['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.commit_message):
            body['commitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.encoding):
            body['encoding'] = request.encoding
        if not UtilClient.is_unset(request.new_path):
            body['newPath'] = request.new_path
        if not UtilClient.is_unset(request.old_path):
            body['oldPath'] = request.old_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFile',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files/update',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_file(
        self,
        repository_id: str,
        request: devops_20210625_models.UpdateFileRequest,
    ) -> devops_20210625_models.UpdateFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_file_with_options(repository_id, request, headers, runtime)

    async def update_file_async(
        self,
        repository_id: str,
        request: devops_20210625_models.UpdateFileRequest,
    ) -> devops_20210625_models.UpdateFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_file_with_options_async(repository_id, request, headers, runtime)

    def update_flow_tag_with_options(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateFlowTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.color):
            query['color'] = request.color
        if not UtilClient.is_unset(request.flow_tag_group_id):
            query['flowTagGroupId'] = request.flow_tag_group_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tags/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateFlowTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_flow_tag_with_options_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateFlowTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.color):
            query['color'] = request.color
        if not UtilClient.is_unset(request.flow_tag_group_id):
            query['flowTagGroupId'] = request.flow_tag_group_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tags/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateFlowTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_flow_tag(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagRequest,
    ) -> devops_20210625_models.UpdateFlowTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_flow_tag_with_options(organization_id, id, request, headers, runtime)

    async def update_flow_tag_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagRequest,
    ) -> devops_20210625_models.UpdateFlowTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_flow_tag_with_options_async(organization_id, id, request, headers, runtime)

    def update_flow_tag_group_with_options(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateFlowTagGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tagGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateFlowTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_flow_tag_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateFlowTagGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tagGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateFlowTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_flow_tag_group(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagGroupRequest,
    ) -> devops_20210625_models.UpdateFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_flow_tag_group_with_options(organization_id, id, request, headers, runtime)

    async def update_flow_tag_group_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagGroupRequest,
    ) -> devops_20210625_models.UpdateFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_flow_tag_group_with_options_async(organization_id, id, request, headers, runtime)

    def update_group_with_options(
        self,
        request: devops_20210625_models.UpdateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.avatar_url):
            body['avatarUrl'] = request.avatar_url
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.path):
            body['path'] = request.path
        if not UtilClient.is_unset(request.path_with_namespace):
            body['pathWithNamespace'] = request.path_with_namespace
        if not UtilClient.is_unset(request.visibility_level):
            body['visibilityLevel'] = request.visibility_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/groups/modify',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_group_with_options_async(
        self,
        request: devops_20210625_models.UpdateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.avatar_url):
            body['avatarUrl'] = request.avatar_url
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.path):
            body['path'] = request.path
        if not UtilClient.is_unset(request.path_with_namespace):
            body['pathWithNamespace'] = request.path_with_namespace
        if not UtilClient.is_unset(request.visibility_level):
            body['visibilityLevel'] = request.visibility_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/groups/modify',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_group(
        self,
        request: devops_20210625_models.UpdateGroupRequest,
    ) -> devops_20210625_models.UpdateGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_group_with_options(request, headers, runtime)

    async def update_group_async(
        self,
        request: devops_20210625_models.UpdateGroupRequest,
    ) -> devops_20210625_models.UpdateGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_group_with_options_async(request, headers, runtime)

    def update_group_member_with_options(
        self,
        group_id: str,
        request: devops_20210625_models.UpdateGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.aliyun_pk):
            query['aliyunPk'] = request.aliyun_pk
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.access_level):
            body['accessLevel'] = request.access_level
        if not UtilClient.is_unset(request.member_type):
            body['memberType'] = request.member_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroupMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/groups/{OpenApiUtilClient.get_encode_param(group_id)}/members/update/aliyun_pk',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_group_member_with_options_async(
        self,
        group_id: str,
        request: devops_20210625_models.UpdateGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.aliyun_pk):
            query['aliyunPk'] = request.aliyun_pk
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.access_level):
            body['accessLevel'] = request.access_level
        if not UtilClient.is_unset(request.member_type):
            body['memberType'] = request.member_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroupMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/groups/{OpenApiUtilClient.get_encode_param(group_id)}/members/update/aliyun_pk',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_group_member(
        self,
        group_id: str,
        request: devops_20210625_models.UpdateGroupMemberRequest,
    ) -> devops_20210625_models.UpdateGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_group_member_with_options(group_id, request, headers, runtime)

    async def update_group_member_async(
        self,
        group_id: str,
        request: devops_20210625_models.UpdateGroupMemberRequest,
    ) -> devops_20210625_models.UpdateGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_group_member_with_options_async(group_id, request, headers, runtime)

    def update_host_group_with_options(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateHostGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateHostGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_region):
            body['aliyunRegion'] = request.aliyun_region
        if not UtilClient.is_unset(request.ecs_label_key):
            body['ecsLabelKey'] = request.ecs_label_key
        if not UtilClient.is_unset(request.ecs_label_value):
            body['ecsLabelValue'] = request.ecs_label_value
        if not UtilClient.is_unset(request.ecs_type):
            body['ecsType'] = request.ecs_type
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.machine_infos):
            body['machineInfos'] = request.machine_infos
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.service_connection_id):
            body['serviceConnectionId'] = request.service_connection_id
        if not UtilClient.is_unset(request.tag_ids):
            body['tagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/hostGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_host_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateHostGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateHostGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_region):
            body['aliyunRegion'] = request.aliyun_region
        if not UtilClient.is_unset(request.ecs_label_key):
            body['ecsLabelKey'] = request.ecs_label_key
        if not UtilClient.is_unset(request.ecs_label_value):
            body['ecsLabelValue'] = request.ecs_label_value
        if not UtilClient.is_unset(request.ecs_type):
            body['ecsType'] = request.ecs_type
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.machine_infos):
            body['machineInfos'] = request.machine_infos
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.service_connection_id):
            body['serviceConnectionId'] = request.service_connection_id
        if not UtilClient.is_unset(request.tag_ids):
            body['tagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/hostGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_host_group(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateHostGroupRequest,
    ) -> devops_20210625_models.UpdateHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_host_group_with_options(organization_id, id, request, headers, runtime)

    async def update_host_group_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateHostGroupRequest,
    ) -> devops_20210625_models.UpdateHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_host_group_with_options_async(organization_id, id, request, headers, runtime)

    def update_merge_request_with_options(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.UpdateMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMergeRequest',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/merge_requests/{OpenApiUtilClient.get_encode_param(local_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateMergeRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_merge_request_with_options_async(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.UpdateMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMergeRequest',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/merge_requests/{OpenApiUtilClient.get_encode_param(local_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateMergeRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_merge_request(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.UpdateMergeRequestRequest,
    ) -> devops_20210625_models.UpdateMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_merge_request_with_options(repository_id, local_id, request, headers, runtime)

    async def update_merge_request_async(
        self,
        repository_id: str,
        local_id: str,
        request: devops_20210625_models.UpdateMergeRequestRequest,
    ) -> devops_20210625_models.UpdateMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_merge_request_with_options_async(repository_id, local_id, request, headers, runtime)

    def update_merge_request_personnel_with_options(
        self,
        repository_id: str,
        local_id: str,
        person_type: str,
        request: devops_20210625_models.UpdateMergeRequestPersonnelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateMergeRequestPersonnelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.new_user_id_list):
            body['newUserIdList'] = request.new_user_id_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMergeRequestPersonnel',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/merge_requests/{OpenApiUtilClient.get_encode_param(local_id)}/person/{OpenApiUtilClient.get_encode_param(person_type)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateMergeRequestPersonnelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_merge_request_personnel_with_options_async(
        self,
        repository_id: str,
        local_id: str,
        person_type: str,
        request: devops_20210625_models.UpdateMergeRequestPersonnelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateMergeRequestPersonnelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.new_user_id_list):
            body['newUserIdList'] = request.new_user_id_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMergeRequestPersonnel',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/merge_requests/{OpenApiUtilClient.get_encode_param(local_id)}/person/{OpenApiUtilClient.get_encode_param(person_type)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateMergeRequestPersonnelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_merge_request_personnel(
        self,
        repository_id: str,
        local_id: str,
        person_type: str,
        request: devops_20210625_models.UpdateMergeRequestPersonnelRequest,
    ) -> devops_20210625_models.UpdateMergeRequestPersonnelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_merge_request_personnel_with_options(repository_id, local_id, person_type, request, headers, runtime)

    async def update_merge_request_personnel_async(
        self,
        repository_id: str,
        local_id: str,
        person_type: str,
        request: devops_20210625_models.UpdateMergeRequestPersonnelRequest,
    ) -> devops_20210625_models.UpdateMergeRequestPersonnelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_merge_request_personnel_with_options_async(repository_id, local_id, person_type, request, headers, runtime)

    def update_pipeline_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdatePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdatePipelineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.pipeline_id):
            body['pipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipeline_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdatePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdatePipelineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.pipeline_id):
            body['pipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pipeline(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdatePipelineRequest,
    ) -> devops_20210625_models.UpdatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipeline_with_options(organization_id, request, headers, runtime)

    async def update_pipeline_async(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdatePipelineRequest,
    ) -> devops_20210625_models.UpdatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_pipeline_with_options_async(organization_id, request, headers, runtime)

    def update_pipeline_base_info_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.UpdatePipelineBaseInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdatePipelineBaseInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_id):
            query['envId'] = request.env_id
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.tag_list):
            query['tagList'] = request.tag_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipelineBaseInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/baseInfo',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePipelineBaseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipeline_base_info_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.UpdatePipelineBaseInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdatePipelineBaseInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_id):
            query['envId'] = request.env_id
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.tag_list):
            query['tagList'] = request.tag_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipelineBaseInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/baseInfo',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePipelineBaseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pipeline_base_info(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.UpdatePipelineBaseInfoRequest,
    ) -> devops_20210625_models.UpdatePipelineBaseInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipeline_base_info_with_options(organization_id, pipeline_id, request, headers, runtime)

    async def update_pipeline_base_info_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.UpdatePipelineBaseInfoRequest,
    ) -> devops_20210625_models.UpdatePipelineBaseInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_pipeline_base_info_with_options_async(organization_id, pipeline_id, request, headers, runtime)

    def update_pipeline_group_with_options(
        self,
        organization_id: str,
        group_id: str,
        request: devops_20210625_models.UpdatePipelineGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdatePipelineGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePipelineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipeline_group_with_options_async(
        self,
        organization_id: str,
        group_id: str,
        request: devops_20210625_models.UpdatePipelineGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdatePipelineGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePipelineGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pipeline_group(
        self,
        organization_id: str,
        group_id: str,
        request: devops_20210625_models.UpdatePipelineGroupRequest,
    ) -> devops_20210625_models.UpdatePipelineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipeline_group_with_options(organization_id, group_id, request, headers, runtime)

    async def update_pipeline_group_async(
        self,
        organization_id: str,
        group_id: str,
        request: devops_20210625_models.UpdatePipelineGroupRequest,
    ) -> devops_20210625_models.UpdatePipelineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_pipeline_group_with_options_async(organization_id, group_id, request, headers, runtime)

    def update_project_field_with_options(
        self,
        organization_id: str,
        identifier: str,
        request: devops_20210625_models.UpdateProjectFieldRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateProjectFieldResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.status_identifier):
            body['statusIdentifier'] = request.status_identifier
        if not UtilClient.is_unset(request.update_basic_field_request_list):
            body['updateBasicFieldRequestList'] = request.update_basic_field_request_list
        if not UtilClient.is_unset(request.update_for_open_api_list):
            body['updateForOpenApiList'] = request.update_for_open_api_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProjectField',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/project/{OpenApiUtilClient.get_encode_param(identifier)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateProjectFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_field_with_options_async(
        self,
        organization_id: str,
        identifier: str,
        request: devops_20210625_models.UpdateProjectFieldRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateProjectFieldResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.status_identifier):
            body['statusIdentifier'] = request.status_identifier
        if not UtilClient.is_unset(request.update_basic_field_request_list):
            body['updateBasicFieldRequestList'] = request.update_basic_field_request_list
        if not UtilClient.is_unset(request.update_for_open_api_list):
            body['updateForOpenApiList'] = request.update_for_open_api_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProjectField',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/project/{OpenApiUtilClient.get_encode_param(identifier)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateProjectFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project_field(
        self,
        organization_id: str,
        identifier: str,
        request: devops_20210625_models.UpdateProjectFieldRequest,
    ) -> devops_20210625_models.UpdateProjectFieldResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_field_with_options(organization_id, identifier, request, headers, runtime)

    async def update_project_field_async(
        self,
        organization_id: str,
        identifier: str,
        request: devops_20210625_models.UpdateProjectFieldRequest,
    ) -> devops_20210625_models.UpdateProjectFieldResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_project_field_with_options_async(organization_id, identifier, request, headers, runtime)

    def update_project_label_with_options(
        self,
        label_id: str,
        request: devops_20210625_models.UpdateProjectLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateProjectLabelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        body = {}
        if not UtilClient.is_unset(request.color):
            body['color'] = request.color
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProjectLabel',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/labels/{OpenApiUtilClient.get_encode_param(label_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateProjectLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_label_with_options_async(
        self,
        label_id: str,
        request: devops_20210625_models.UpdateProjectLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateProjectLabelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.repository_identity):
            query['repositoryIdentity'] = request.repository_identity
        body = {}
        if not UtilClient.is_unset(request.color):
            body['color'] = request.color
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProjectLabel',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/labels/{OpenApiUtilClient.get_encode_param(label_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateProjectLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project_label(
        self,
        label_id: str,
        request: devops_20210625_models.UpdateProjectLabelRequest,
    ) -> devops_20210625_models.UpdateProjectLabelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_label_with_options(label_id, request, headers, runtime)

    async def update_project_label_async(
        self,
        label_id: str,
        request: devops_20210625_models.UpdateProjectLabelRequest,
    ) -> devops_20210625_models.UpdateProjectLabelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_project_label_with_options_async(label_id, request, headers, runtime)

    def update_project_member_with_options(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.UpdateProjectMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateProjectMemberResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_identifier):
            body['roleIdentifier'] = request.role_identifier
        if not UtilClient.is_unset(request.target_identifier):
            body['targetIdentifier'] = request.target_identifier
        if not UtilClient.is_unset(request.target_type):
            body['targetType'] = request.target_type
        if not UtilClient.is_unset(request.user_identifier):
            body['userIdentifier'] = request.user_identifier
        if not UtilClient.is_unset(request.user_type):
            body['userType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProjectMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/updateMember',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateProjectMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_member_with_options_async(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.UpdateProjectMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateProjectMemberResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_identifier):
            body['roleIdentifier'] = request.role_identifier
        if not UtilClient.is_unset(request.target_identifier):
            body['targetIdentifier'] = request.target_identifier
        if not UtilClient.is_unset(request.target_type):
            body['targetType'] = request.target_type
        if not UtilClient.is_unset(request.user_identifier):
            body['userIdentifier'] = request.user_identifier
        if not UtilClient.is_unset(request.user_type):
            body['userType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProjectMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/updateMember',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateProjectMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project_member(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.UpdateProjectMemberRequest,
    ) -> devops_20210625_models.UpdateProjectMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_member_with_options(organization_id, project_id, request, headers, runtime)

    async def update_project_member_async(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.UpdateProjectMemberRequest,
    ) -> devops_20210625_models.UpdateProjectMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_project_member_with_options_async(organization_id, project_id, request, headers, runtime)

    def update_protected_branches_with_options(
        self,
        repository_id: str,
        id: str,
        request: devops_20210625_models.UpdateProtectedBranchesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateProtectedBranchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.allow_merge_roles):
            body['allowMergeRoles'] = request.allow_merge_roles
        if not UtilClient.is_unset(request.allow_merge_user_ids):
            body['allowMergeUserIds'] = request.allow_merge_user_ids
        if not UtilClient.is_unset(request.allow_push_roles):
            body['allowPushRoles'] = request.allow_push_roles
        if not UtilClient.is_unset(request.allow_push_user_ids):
            body['allowPushUserIds'] = request.allow_push_user_ids
        if not UtilClient.is_unset(request.branch):
            body['branch'] = request.branch
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.merge_request_setting):
            body['mergeRequestSetting'] = request.merge_request_setting
        if not UtilClient.is_unset(request.test_setting_dto):
            body['testSettingDTO'] = request.test_setting_dto
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProtectedBranches',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(repository_id)}/protect_branches/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateProtectedBranchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_protected_branches_with_options_async(
        self,
        repository_id: str,
        id: str,
        request: devops_20210625_models.UpdateProtectedBranchesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateProtectedBranchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.allow_merge_roles):
            body['allowMergeRoles'] = request.allow_merge_roles
        if not UtilClient.is_unset(request.allow_merge_user_ids):
            body['allowMergeUserIds'] = request.allow_merge_user_ids
        if not UtilClient.is_unset(request.allow_push_roles):
            body['allowPushRoles'] = request.allow_push_roles
        if not UtilClient.is_unset(request.allow_push_user_ids):
            body['allowPushUserIds'] = request.allow_push_user_ids
        if not UtilClient.is_unset(request.branch):
            body['branch'] = request.branch
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.merge_request_setting):
            body['mergeRequestSetting'] = request.merge_request_setting
        if not UtilClient.is_unset(request.test_setting_dto):
            body['testSettingDTO'] = request.test_setting_dto
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProtectedBranches',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(repository_id)}/protect_branches/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateProtectedBranchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_protected_branches(
        self,
        repository_id: str,
        id: str,
        request: devops_20210625_models.UpdateProtectedBranchesRequest,
    ) -> devops_20210625_models.UpdateProtectedBranchesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_protected_branches_with_options(repository_id, id, request, headers, runtime)

    async def update_protected_branches_async(
        self,
        repository_id: str,
        id: str,
        request: devops_20210625_models.UpdateProtectedBranchesRequest,
    ) -> devops_20210625_models.UpdateProtectedBranchesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_protected_branches_with_options_async(repository_id, id, request, headers, runtime)

    def update_push_review_on_off_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.UpdatePushReviewOnOffRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdatePushReviewOnOffResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.trunk_mode):
            query['trunkMode'] = request.trunk_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePushReviewOnOff',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/settings/trunk_mode',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePushReviewOnOffResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_push_review_on_off_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.UpdatePushReviewOnOffRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdatePushReviewOnOffResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.trunk_mode):
            query['trunkMode'] = request.trunk_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePushReviewOnOff',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/settings/trunk_mode',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePushReviewOnOffResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_push_review_on_off(
        self,
        repository_id: str,
        request: devops_20210625_models.UpdatePushReviewOnOffRequest,
    ) -> devops_20210625_models.UpdatePushReviewOnOffResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_push_review_on_off_with_options(repository_id, request, headers, runtime)

    async def update_push_review_on_off_async(
        self,
        repository_id: str,
        request: devops_20210625_models.UpdatePushReviewOnOffRequest,
    ) -> devops_20210625_models.UpdatePushReviewOnOffResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_push_review_on_off_with_options_async(repository_id, request, headers, runtime)

    def update_push_rule_with_options(
        self,
        repository_id: str,
        push_rule_id: str,
        request: devops_20210625_models.UpdatePushRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdatePushRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.rule_infos):
            body['ruleInfos'] = request.rule_infos
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePushRule',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/push_rule/{OpenApiUtilClient.get_encode_param(push_rule_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePushRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_push_rule_with_options_async(
        self,
        repository_id: str,
        push_rule_id: str,
        request: devops_20210625_models.UpdatePushRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdatePushRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.rule_infos):
            body['ruleInfos'] = request.rule_infos
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePushRule',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(repository_id)}/push_rule/{OpenApiUtilClient.get_encode_param(push_rule_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePushRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_push_rule(
        self,
        repository_id: str,
        push_rule_id: str,
        request: devops_20210625_models.UpdatePushRuleRequest,
    ) -> devops_20210625_models.UpdatePushRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_push_rule_with_options(repository_id, push_rule_id, request, headers, runtime)

    async def update_push_rule_async(
        self,
        repository_id: str,
        push_rule_id: str,
        request: devops_20210625_models.UpdatePushRuleRequest,
    ) -> devops_20210625_models.UpdatePushRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_push_rule_with_options_async(repository_id, push_rule_id, request, headers, runtime)

    def update_repository_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.UpdateRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.admin_setting_language):
            body['adminSettingLanguage'] = request.admin_setting_language
        if not UtilClient.is_unset(request.avatar):
            body['avatar'] = request.avatar
        if not UtilClient.is_unset(request.builds_enabled):
            body['buildsEnabled'] = request.builds_enabled
        if not UtilClient.is_unset(request.check_email):
            body['checkEmail'] = request.check_email
        if not UtilClient.is_unset(request.default_branch):
            body['defaultBranch'] = request.default_branch
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.issues_enabled):
            body['issuesEnabled'] = request.issues_enabled
        if not UtilClient.is_unset(request.merge_requests_enabled):
            body['mergeRequestsEnabled'] = request.merge_requests_enabled
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.open_clone_download_control):
            body['openCloneDownloadControl'] = request.open_clone_download_control
        if not UtilClient.is_unset(request.path):
            body['path'] = request.path
        if not UtilClient.is_unset(request.project_clone_download_method_list):
            body['projectCloneDownloadMethodList'] = request.project_clone_download_method_list
        if not UtilClient.is_unset(request.project_clone_download_role_list):
            body['projectCloneDownloadRoleList'] = request.project_clone_download_role_list
        if not UtilClient.is_unset(request.snippets_enabled):
            body['snippetsEnabled'] = request.snippets_enabled
        if not UtilClient.is_unset(request.visibility_level):
            body['visibilityLevel'] = request.visibility_level
        if not UtilClient.is_unset(request.wiki_enabled):
            body['wikiEnabled'] = request.wiki_enabled
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_repository_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.UpdateRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.admin_setting_language):
            body['adminSettingLanguage'] = request.admin_setting_language
        if not UtilClient.is_unset(request.avatar):
            body['avatar'] = request.avatar
        if not UtilClient.is_unset(request.builds_enabled):
            body['buildsEnabled'] = request.builds_enabled
        if not UtilClient.is_unset(request.check_email):
            body['checkEmail'] = request.check_email
        if not UtilClient.is_unset(request.default_branch):
            body['defaultBranch'] = request.default_branch
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.issues_enabled):
            body['issuesEnabled'] = request.issues_enabled
        if not UtilClient.is_unset(request.merge_requests_enabled):
            body['mergeRequestsEnabled'] = request.merge_requests_enabled
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.open_clone_download_control):
            body['openCloneDownloadControl'] = request.open_clone_download_control
        if not UtilClient.is_unset(request.path):
            body['path'] = request.path
        if not UtilClient.is_unset(request.project_clone_download_method_list):
            body['projectCloneDownloadMethodList'] = request.project_clone_download_method_list
        if not UtilClient.is_unset(request.project_clone_download_role_list):
            body['projectCloneDownloadRoleList'] = request.project_clone_download_role_list
        if not UtilClient.is_unset(request.snippets_enabled):
            body['snippetsEnabled'] = request.snippets_enabled
        if not UtilClient.is_unset(request.visibility_level):
            body['visibilityLevel'] = request.visibility_level
        if not UtilClient.is_unset(request.wiki_enabled):
            body['wikiEnabled'] = request.wiki_enabled
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_repository(
        self,
        repository_id: str,
        request: devops_20210625_models.UpdateRepositoryRequest,
    ) -> devops_20210625_models.UpdateRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_repository_with_options(repository_id, request, headers, runtime)

    async def update_repository_async(
        self,
        repository_id: str,
        request: devops_20210625_models.UpdateRepositoryRequest,
    ) -> devops_20210625_models.UpdateRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_repository_with_options_async(repository_id, request, headers, runtime)

    def update_repository_member_with_options(
        self,
        repository_id: str,
        aliyun_pk: str,
        request: devops_20210625_models.UpdateRepositoryMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateRepositoryMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.access_level):
            body['accessLevel'] = request.access_level
        if not UtilClient.is_unset(request.expire_at):
            body['expireAt'] = request.expire_at
        if not UtilClient.is_unset(request.member_type):
            body['memberType'] = request.member_type
        if not UtilClient.is_unset(request.related_id):
            body['relatedId'] = request.related_id
        if not UtilClient.is_unset(request.related_infos):
            body['relatedInfos'] = request.related_infos
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRepositoryMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/members/{OpenApiUtilClient.get_encode_param(aliyun_pk)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateRepositoryMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_repository_member_with_options_async(
        self,
        repository_id: str,
        aliyun_pk: str,
        request: devops_20210625_models.UpdateRepositoryMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateRepositoryMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.access_level):
            body['accessLevel'] = request.access_level
        if not UtilClient.is_unset(request.expire_at):
            body['expireAt'] = request.expire_at
        if not UtilClient.is_unset(request.member_type):
            body['memberType'] = request.member_type
        if not UtilClient.is_unset(request.related_id):
            body['relatedId'] = request.related_id
        if not UtilClient.is_unset(request.related_infos):
            body['relatedInfos'] = request.related_infos
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRepositoryMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/members/{OpenApiUtilClient.get_encode_param(aliyun_pk)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateRepositoryMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_repository_member(
        self,
        repository_id: str,
        aliyun_pk: str,
        request: devops_20210625_models.UpdateRepositoryMemberRequest,
    ) -> devops_20210625_models.UpdateRepositoryMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_repository_member_with_options(repository_id, aliyun_pk, request, headers, runtime)

    async def update_repository_member_async(
        self,
        repository_id: str,
        aliyun_pk: str,
        request: devops_20210625_models.UpdateRepositoryMemberRequest,
    ) -> devops_20210625_models.UpdateRepositoryMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_repository_member_with_options_async(repository_id, aliyun_pk, request, headers, runtime)

    def update_resource_member_with_options(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
        request: devops_20210625_models.UpdateResourceMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateResourceMemberResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(resource_type)}/{OpenApiUtilClient.get_encode_param(resource_id)}/members/{OpenApiUtilClient.get_encode_param(account_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateResourceMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_member_with_options_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
        request: devops_20210625_models.UpdateResourceMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateResourceMemberResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(resource_type)}/{OpenApiUtilClient.get_encode_param(resource_id)}/members/{OpenApiUtilClient.get_encode_param(account_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateResourceMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_member(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
        request: devops_20210625_models.UpdateResourceMemberRequest,
    ) -> devops_20210625_models.UpdateResourceMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_member_with_options(organization_id, resource_type, resource_id, account_id, request, headers, runtime)

    async def update_resource_member_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
        request: devops_20210625_models.UpdateResourceMemberRequest,
    ) -> devops_20210625_models.UpdateResourceMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_resource_member_with_options_async(organization_id, resource_type, resource_id, account_id, request, headers, runtime)

    def update_test_case_with_options(
        self,
        organization_id: str,
        testcase_identifier: str,
        request: devops_20210625_models.UpdateTestCaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateTestCaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.update_workitem_property_request):
            body['updateWorkitemPropertyRequest'] = request.update_workitem_property_request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTestCase',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/testhub/testcase/{OpenApiUtilClient.get_encode_param(testcase_identifier)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateTestCaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_test_case_with_options_async(
        self,
        organization_id: str,
        testcase_identifier: str,
        request: devops_20210625_models.UpdateTestCaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateTestCaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.update_workitem_property_request):
            body['updateWorkitemPropertyRequest'] = request.update_workitem_property_request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTestCase',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/testhub/testcase/{OpenApiUtilClient.get_encode_param(testcase_identifier)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateTestCaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_test_case(
        self,
        organization_id: str,
        testcase_identifier: str,
        request: devops_20210625_models.UpdateTestCaseRequest,
    ) -> devops_20210625_models.UpdateTestCaseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_test_case_with_options(organization_id, testcase_identifier, request, headers, runtime)

    async def update_test_case_async(
        self,
        organization_id: str,
        testcase_identifier: str,
        request: devops_20210625_models.UpdateTestCaseRequest,
    ) -> devops_20210625_models.UpdateTestCaseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_test_case_with_options_async(organization_id, testcase_identifier, request, headers, runtime)

    def update_test_result_with_options(
        self,
        organization_id: str,
        test_plan_identifier: str,
        testcase_identifier: str,
        request: devops_20210625_models.UpdateTestResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateTestResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.executor):
            body['executor'] = request.executor
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTestResult',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/testhub/testplan/{OpenApiUtilClient.get_encode_param(test_plan_identifier)}/testresult/{OpenApiUtilClient.get_encode_param(testcase_identifier)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateTestResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_test_result_with_options_async(
        self,
        organization_id: str,
        test_plan_identifier: str,
        testcase_identifier: str,
        request: devops_20210625_models.UpdateTestResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateTestResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.executor):
            body['executor'] = request.executor
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTestResult',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/testhub/testplan/{OpenApiUtilClient.get_encode_param(test_plan_identifier)}/testresult/{OpenApiUtilClient.get_encode_param(testcase_identifier)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateTestResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_test_result(
        self,
        organization_id: str,
        test_plan_identifier: str,
        testcase_identifier: str,
        request: devops_20210625_models.UpdateTestResultRequest,
    ) -> devops_20210625_models.UpdateTestResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_test_result_with_options(organization_id, test_plan_identifier, testcase_identifier, request, headers, runtime)

    async def update_test_result_async(
        self,
        organization_id: str,
        test_plan_identifier: str,
        testcase_identifier: str,
        request: devops_20210625_models.UpdateTestResultRequest,
    ) -> devops_20210625_models.UpdateTestResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_test_result_with_options_async(organization_id, test_plan_identifier, testcase_identifier, request, headers, runtime)

    def update_variable_group_with_options(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateVariableGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateVariableGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/variableGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateVariableGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_variable_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateVariableGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateVariableGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/variableGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateVariableGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_variable_group(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateVariableGroupRequest,
    ) -> devops_20210625_models.UpdateVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_variable_group_with_options(organization_id, id, request, headers, runtime)

    async def update_variable_group_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateVariableGroupRequest,
    ) -> devops_20210625_models.UpdateVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_variable_group_with_options_async(organization_id, id, request, headers, runtime)

    def update_work_item_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdateWorkItemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateWorkItemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.field_type):
            body['fieldType'] = request.field_type
        if not UtilClient.is_unset(request.identifier):
            body['identifier'] = request.identifier
        if not UtilClient.is_unset(request.property_key):
            body['propertyKey'] = request.property_key
        if not UtilClient.is_unset(request.property_value):
            body['propertyValue'] = request.property_value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkItem',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateWorkItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_work_item_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdateWorkItemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateWorkItemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.field_type):
            body['fieldType'] = request.field_type
        if not UtilClient.is_unset(request.identifier):
            body['identifier'] = request.identifier
        if not UtilClient.is_unset(request.property_key):
            body['propertyKey'] = request.property_key
        if not UtilClient.is_unset(request.property_value):
            body['propertyValue'] = request.property_value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkItem',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateWorkItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_work_item(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdateWorkItemRequest,
    ) -> devops_20210625_models.UpdateWorkItemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_work_item_with_options(organization_id, request, headers, runtime)

    async def update_work_item_async(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdateWorkItemRequest,
    ) -> devops_20210625_models.UpdateWorkItemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_work_item_with_options_async(organization_id, request, headers, runtime)

    def update_workitem_comment_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdateWorkitemCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateWorkitemCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment_id):
            body['commentId'] = request.comment_id
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.format_type):
            body['formatType'] = request.format_type
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkitemComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/commentUpdate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateWorkitemCommentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workitem_comment_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdateWorkitemCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateWorkitemCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment_id):
            body['commentId'] = request.comment_id
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.format_type):
            body['formatType'] = request.format_type
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkitemComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/commentUpdate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateWorkitemCommentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workitem_comment(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdateWorkitemCommentRequest,
    ) -> devops_20210625_models.UpdateWorkitemCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_workitem_comment_with_options(organization_id, request, headers, runtime)

    async def update_workitem_comment_async(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdateWorkitemCommentRequest,
    ) -> devops_20210625_models.UpdateWorkitemCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_workitem_comment_with_options_async(organization_id, request, headers, runtime)

    def update_workitem_field_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdateWorkitemFieldRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateWorkitemFieldResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.update_workitem_property_request):
            body['updateWorkitemPropertyRequest'] = request.update_workitem_property_request
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkitemField',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/updateWorkitemField',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateWorkitemFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workitem_field_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdateWorkitemFieldRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateWorkitemFieldResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.update_workitem_property_request):
            body['updateWorkitemPropertyRequest'] = request.update_workitem_property_request
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkitemField',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/updateWorkitemField',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateWorkitemFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workitem_field(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdateWorkitemFieldRequest,
    ) -> devops_20210625_models.UpdateWorkitemFieldResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_workitem_field_with_options(organization_id, request, headers, runtime)

    async def update_workitem_field_async(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdateWorkitemFieldRequest,
    ) -> devops_20210625_models.UpdateWorkitemFieldResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_workitem_field_with_options_async(organization_id, request, headers, runtime)

    def workitem_attachment_create_with_options(
        self,
        organization_id: str,
        workitem_identifier: str,
        request: devops_20210625_models.WorkitemAttachmentCreateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.WorkitemAttachmentCreateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_key):
            body['fileKey'] = request.file_key
        if not UtilClient.is_unset(request.original_filename):
            body['originalFilename'] = request.original_filename
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='WorkitemAttachmentCreate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitem/{OpenApiUtilClient.get_encode_param(workitem_identifier)}/attachment',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.WorkitemAttachmentCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def workitem_attachment_create_with_options_async(
        self,
        organization_id: str,
        workitem_identifier: str,
        request: devops_20210625_models.WorkitemAttachmentCreateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.WorkitemAttachmentCreateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_key):
            body['fileKey'] = request.file_key
        if not UtilClient.is_unset(request.original_filename):
            body['originalFilename'] = request.original_filename
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='WorkitemAttachmentCreate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitem/{OpenApiUtilClient.get_encode_param(workitem_identifier)}/attachment',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.WorkitemAttachmentCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def workitem_attachment_create(
        self,
        organization_id: str,
        workitem_identifier: str,
        request: devops_20210625_models.WorkitemAttachmentCreateRequest,
    ) -> devops_20210625_models.WorkitemAttachmentCreateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.workitem_attachment_create_with_options(organization_id, workitem_identifier, request, headers, runtime)

    async def workitem_attachment_create_async(
        self,
        organization_id: str,
        workitem_identifier: str,
        request: devops_20210625_models.WorkitemAttachmentCreateRequest,
    ) -> devops_20210625_models.WorkitemAttachmentCreateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.workitem_attachment_create_with_options_async(organization_id, workitem_identifier, request, headers, runtime)
