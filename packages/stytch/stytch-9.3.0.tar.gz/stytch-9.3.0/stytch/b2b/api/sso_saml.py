# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, List, Optional

from stytch.b2b.models.sso import (
    SAMLConnectionImplicitRoleAssignment,
    SAMLGroupImplicitRoleAssignment,
)
from stytch.b2b.models.sso_saml import (
    CreateConnectionRequestOptions,
    CreateConnectionResponse,
    DeleteVerificationCertificateRequestOptions,
    DeleteVerificationCertificateResponse,
    UpdateByURLRequestOptions,
    UpdateByURLResponse,
    UpdateConnectionRequestOptions,
    UpdateConnectionResponse,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class SAML:
    def __init__(
        self, api_base: ApiBase, sync_client: SyncClient, async_client: AsyncClient
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def create_connection(
        self,
        organization_id: str,
        display_name: Optional[str] = None,
        method_options: Optional[CreateConnectionRequestOptions] = None,
    ) -> CreateConnectionResponse:
        """Create a new SAML Connection. /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - display_name: A human-readable display name for the connection.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }
        if display_name is not None:
            data["display_name"] = display_name

        url = self.api_base.url_for("/v1/b2b/sso/saml/{organization_id}", data)
        res = self.sync_client.post(url, data, headers)
        return CreateConnectionResponse.from_json(res.response.status_code, res.json)

    async def create_connection_async(
        self,
        organization_id: str,
        display_name: Optional[str] = None,
        method_options: Optional[CreateConnectionRequestOptions] = None,
    ) -> CreateConnectionResponse:
        """Create a new SAML Connection. /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - display_name: A human-readable display name for the connection.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }
        if display_name is not None:
            data["display_name"] = display_name

        url = self.api_base.url_for("/v1/b2b/sso/saml/{organization_id}", data)
        res = await self.async_client.post(url, data, headers)
        return CreateConnectionResponse.from_json(res.response.status, res.json)

    def update_connection(
        self,
        organization_id: str,
        connection_id: str,
        idp_entity_id: Optional[str] = None,
        display_name: Optional[str] = None,
        attribute_mapping: Optional[Dict[str, Any]] = None,
        x509_certificate: Optional[str] = None,
        idp_sso_url: Optional[str] = None,
        saml_connection_implicit_role_assignments: Optional[
            List[SAMLConnectionImplicitRoleAssignment]
        ] = None,
        saml_group_implicit_role_assignments: Optional[
            List[SAMLGroupImplicitRoleAssignment]
        ] = None,
        alternative_audience_uri: Optional[str] = None,
        method_options: Optional[UpdateConnectionRequestOptions] = None,
    ) -> UpdateConnectionResponse:
        """Updates an existing SAML connection.

        Note that a newly created connection will not become active until all of the following are provided:
        * `idp_sso_url`
        * `attribute_mapping`
        * `idp_entity_id`
        * `x509_certificate`
         /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - connection_id: Globally unique UUID that identifies a specific SSO `connection_id` for a Member.
          - idp_entity_id: A globally unique name for the IdP. This will be provided by the IdP.
          - display_name: A human-readable display name for the connection.
          - attribute_mapping: An object that represents the attributes used to identify a Member. This object will map the IdP-defined User attributes to Stytch-specific values. Required attributes: `email` and one of `full_name` or `first_name` and `last_name`.
          - x509_certificate: A certificate that Stytch will use to verify the sign-in assertion sent by the IdP, in [PEM](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail) format. See our [X509 guide](https://stytch.com/docs/b2b/api/saml-certificates) for more info.
          - idp_sso_url: The URL for which assertions for login requests will be sent. This will be provided by the IdP.
          - saml_connection_implicit_role_assignments: All Members who log in with this SAML connection will implicitly receive the specified Roles. See the [RBAC guide](https://stytch.com/docs/b2b/guides/rbac/role-assignment) for more information about role assignment.
          - saml_group_implicit_role_assignments: Defines the names of the SAML groups
         that grant specific role assignments. For each group-Role pair, if a Member logs in with this SAML connection and
         belongs to the specified SAML group, they will be granted the associated Role. See the
         [RBAC guide](https://stytch.com/docs/b2b/guides/rbac/role-assignment) for more information about role assignment.
                 Before adding any group implicit role assignments, you must add a "groups" key to your SAML connection's
                 `attribute_mapping`. Make sure that your IdP is configured to correctly send the group information.
          - alternative_audience_uri: An alternative URL to use for the Audience Restriction. This value can be used when you wish to migrate an existing SAML integration to Stytch with zero downtime.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }
        if idp_entity_id is not None:
            data["idp_entity_id"] = idp_entity_id
        if display_name is not None:
            data["display_name"] = display_name
        if attribute_mapping is not None:
            data["attribute_mapping"] = attribute_mapping
        if x509_certificate is not None:
            data["x509_certificate"] = x509_certificate
        if idp_sso_url is not None:
            data["idp_sso_url"] = idp_sso_url
        if saml_connection_implicit_role_assignments is not None:
            data["saml_connection_implicit_role_assignments"] = [
                item.dict() for item in saml_connection_implicit_role_assignments
            ]
        if saml_group_implicit_role_assignments is not None:
            data["saml_group_implicit_role_assignments"] = [
                item.dict() for item in saml_group_implicit_role_assignments
            ]
        if alternative_audience_uri is not None:
            data["alternative_audience_uri"] = alternative_audience_uri

        url = self.api_base.url_for(
            "/v1/b2b/sso/saml/{organization_id}/connections/{connection_id}", data
        )
        res = self.sync_client.put(url, data, headers)
        return UpdateConnectionResponse.from_json(res.response.status_code, res.json)

    async def update_connection_async(
        self,
        organization_id: str,
        connection_id: str,
        idp_entity_id: Optional[str] = None,
        display_name: Optional[str] = None,
        attribute_mapping: Optional[Dict[str, Any]] = None,
        x509_certificate: Optional[str] = None,
        idp_sso_url: Optional[str] = None,
        saml_connection_implicit_role_assignments: Optional[
            List[SAMLConnectionImplicitRoleAssignment]
        ] = None,
        saml_group_implicit_role_assignments: Optional[
            List[SAMLGroupImplicitRoleAssignment]
        ] = None,
        alternative_audience_uri: Optional[str] = None,
        method_options: Optional[UpdateConnectionRequestOptions] = None,
    ) -> UpdateConnectionResponse:
        """Updates an existing SAML connection.

        Note that a newly created connection will not become active until all of the following are provided:
        * `idp_sso_url`
        * `attribute_mapping`
        * `idp_entity_id`
        * `x509_certificate`
         /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - connection_id: Globally unique UUID that identifies a specific SSO `connection_id` for a Member.
          - idp_entity_id: A globally unique name for the IdP. This will be provided by the IdP.
          - display_name: A human-readable display name for the connection.
          - attribute_mapping: An object that represents the attributes used to identify a Member. This object will map the IdP-defined User attributes to Stytch-specific values. Required attributes: `email` and one of `full_name` or `first_name` and `last_name`.
          - x509_certificate: A certificate that Stytch will use to verify the sign-in assertion sent by the IdP, in [PEM](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail) format. See our [X509 guide](https://stytch.com/docs/b2b/api/saml-certificates) for more info.
          - idp_sso_url: The URL for which assertions for login requests will be sent. This will be provided by the IdP.
          - saml_connection_implicit_role_assignments: All Members who log in with this SAML connection will implicitly receive the specified Roles. See the [RBAC guide](https://stytch.com/docs/b2b/guides/rbac/role-assignment) for more information about role assignment.
          - saml_group_implicit_role_assignments: Defines the names of the SAML groups
         that grant specific role assignments. For each group-Role pair, if a Member logs in with this SAML connection and
         belongs to the specified SAML group, they will be granted the associated Role. See the
         [RBAC guide](https://stytch.com/docs/b2b/guides/rbac/role-assignment) for more information about role assignment.
                 Before adding any group implicit role assignments, you must add a "groups" key to your SAML connection's
                 `attribute_mapping`. Make sure that your IdP is configured to correctly send the group information.
          - alternative_audience_uri: An alternative URL to use for the Audience Restriction. This value can be used when you wish to migrate an existing SAML integration to Stytch with zero downtime.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }
        if idp_entity_id is not None:
            data["idp_entity_id"] = idp_entity_id
        if display_name is not None:
            data["display_name"] = display_name
        if attribute_mapping is not None:
            data["attribute_mapping"] = attribute_mapping
        if x509_certificate is not None:
            data["x509_certificate"] = x509_certificate
        if idp_sso_url is not None:
            data["idp_sso_url"] = idp_sso_url
        if saml_connection_implicit_role_assignments is not None:
            data["saml_connection_implicit_role_assignments"] = [
                item.dict() for item in saml_connection_implicit_role_assignments
            ]
        if saml_group_implicit_role_assignments is not None:
            data["saml_group_implicit_role_assignments"] = [
                item.dict() for item in saml_group_implicit_role_assignments
            ]
        if alternative_audience_uri is not None:
            data["alternative_audience_uri"] = alternative_audience_uri

        url = self.api_base.url_for(
            "/v1/b2b/sso/saml/{organization_id}/connections/{connection_id}", data
        )
        res = await self.async_client.put(url, data, headers)
        return UpdateConnectionResponse.from_json(res.response.status, res.json)

    def update_by_url(
        self,
        organization_id: str,
        connection_id: str,
        metadata_url: str,
        method_options: Optional[UpdateByURLRequestOptions] = None,
    ) -> UpdateByURLResponse:
        """Used to update an existing SAML connection using an IDP metadata URL.

        A newly created connection will not become active until all the following are provided:
        * `idp_sso_url`
        * `idp_entity_id`
        * `x509_certificate`
        * `attribute_mapping` (must be supplied using [Update SAML Connection](update-saml-connection))
         /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - connection_id: Globally unique UUID that identifies a specific SSO `connection_id` for a Member.
          - metadata_url: A URL that points to the IdP metadata. This will be provided by the IdP.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
            "metadata_url": metadata_url,
        }

        url = self.api_base.url_for(
            "/v1/b2b/sso/saml/{organization_id}/connections/{connection_id}/url", data
        )
        res = self.sync_client.put(url, data, headers)
        return UpdateByURLResponse.from_json(res.response.status_code, res.json)

    async def update_by_url_async(
        self,
        organization_id: str,
        connection_id: str,
        metadata_url: str,
        method_options: Optional[UpdateByURLRequestOptions] = None,
    ) -> UpdateByURLResponse:
        """Used to update an existing SAML connection using an IDP metadata URL.

        A newly created connection will not become active until all the following are provided:
        * `idp_sso_url`
        * `idp_entity_id`
        * `x509_certificate`
        * `attribute_mapping` (must be supplied using [Update SAML Connection](update-saml-connection))
         /%}

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - connection_id: Globally unique UUID that identifies a specific SSO `connection_id` for a Member.
          - metadata_url: A URL that points to the IdP metadata. This will be provided by the IdP.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
            "metadata_url": metadata_url,
        }

        url = self.api_base.url_for(
            "/v1/b2b/sso/saml/{organization_id}/connections/{connection_id}/url", data
        )
        res = await self.async_client.put(url, data, headers)
        return UpdateByURLResponse.from_json(res.response.status, res.json)

    def delete_verification_certificate(
        self,
        organization_id: str,
        connection_id: str,
        certificate_id: str,
        method_options: Optional[DeleteVerificationCertificateRequestOptions] = None,
    ) -> DeleteVerificationCertificateResponse:
        """Delete a SAML verification certificate.

        You may need to do this when rotating certificates from your IdP, since Stytch allows a maximum of 5 certificates per connection. There must always be at least one certificate per active connection.
         /%}

        Fields:
          - organization_id: The organization ID that the SAML connection belongs to.
          - connection_id: The ID of the SAML connection.
          - certificate_id: The ID of the certificate to be deleted.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
            "certificate_id": certificate_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/sso/saml/{organization_id}/connections/{connection_id}/verification_certificates/{certificate_id}",
            data,
        )
        res = self.sync_client.delete(url, headers)
        return DeleteVerificationCertificateResponse.from_json(
            res.response.status_code, res.json
        )

    async def delete_verification_certificate_async(
        self,
        organization_id: str,
        connection_id: str,
        certificate_id: str,
        method_options: Optional[DeleteVerificationCertificateRequestOptions] = None,
    ) -> DeleteVerificationCertificateResponse:
        """Delete a SAML verification certificate.

        You may need to do this when rotating certificates from your IdP, since Stytch allows a maximum of 5 certificates per connection. There must always be at least one certificate per active connection.
         /%}

        Fields:
          - organization_id: The organization ID that the SAML connection belongs to.
          - connection_id: The ID of the SAML connection.
          - certificate_id: The ID of the certificate to be deleted.
        """  # noqa
        headers: Dict[str, str] = {}
        if method_options is not None:
            headers = method_options.add_headers(headers)
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
            "certificate_id": certificate_id,
        }

        url = self.api_base.url_for(
            "/v1/b2b/sso/saml/{organization_id}/connections/{connection_id}/verification_certificates/{certificate_id}",
            data,
        )
        res = await self.async_client.delete(url, headers)
        return DeleteVerificationCertificateResponse.from_json(
            res.response.status, res.json
        )
