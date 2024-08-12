/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernIr from "../../../../api/index";
import * as core from "../../../../core";
import { EndpointId } from "../../commons/types/EndpointId";
import { EndpointName } from "./EndpointName";
import { HttpMethod } from "./HttpMethod";
import { HttpHeader } from "./HttpHeader";
import { EnvironmentBaseUrlId } from "../../environment/types/EnvironmentBaseUrlId";
import { HttpPath } from "./HttpPath";
import { PathParameter } from "./PathParameter";
import { QueryParameter } from "./QueryParameter";
import { HttpRequestBody } from "./HttpRequestBody";
import { SdkRequest } from "./SdkRequest";
import { HttpResponse } from "./HttpResponse";
import { ResponseErrors } from "./ResponseErrors";
import { Pagination } from "./Pagination";
import { UserSpecifiedEndpointExample } from "./UserSpecifiedEndpointExample";
import { AutogeneratedEndpointExample } from "./AutogeneratedEndpointExample";
import { Declaration } from "../../commons/types/Declaration";
import { ResponseError } from "./ResponseError";

export const HttpEndpoint: core.serialization.ObjectSchema<serializers.HttpEndpoint.Raw, FernIr.HttpEndpoint> =
    core.serialization
        .objectWithoutOptionalProperties({
            id: EndpointId,
            name: EndpointName,
            displayName: core.serialization.string().optional(),
            method: HttpMethod,
            headers: core.serialization.list(HttpHeader),
            baseUrl: EnvironmentBaseUrlId.optional(),
            path: HttpPath,
            fullPath: HttpPath,
            pathParameters: core.serialization.list(PathParameter),
            allPathParameters: core.serialization.list(PathParameter),
            queryParameters: core.serialization.list(QueryParameter),
            requestBody: HttpRequestBody.optional(),
            sdkRequest: SdkRequest.optional(),
            response: HttpResponse.optional(),
            errors: ResponseErrors,
            auth: core.serialization.boolean(),
            idempotent: core.serialization.boolean(),
            pagination: Pagination.optional(),
            userSpecifiedExamples: core.serialization.list(UserSpecifiedEndpointExample),
            autogeneratedExamples: core.serialization.list(AutogeneratedEndpointExample),
        })
        .extend(Declaration);

export declare namespace HttpEndpoint {
    interface Raw extends Declaration.Raw {
        id: EndpointId.Raw;
        name: EndpointName.Raw;
        displayName?: string | null;
        method: HttpMethod.Raw;
        headers: HttpHeader.Raw[];
        baseUrl?: EnvironmentBaseUrlId.Raw | null;
        path: HttpPath.Raw;
        fullPath: HttpPath.Raw;
        pathParameters: PathParameter.Raw[];
        allPathParameters: PathParameter.Raw[];
        queryParameters: QueryParameter.Raw[];
        requestBody?: HttpRequestBody.Raw | null;
        sdkRequest?: SdkRequest.Raw | null;
        response?: HttpResponse.Raw | null;
        errors: ResponseErrors.Raw;
        auth: boolean;
        idempotent: boolean;
        pagination?: Pagination.Raw | null;
        userSpecifiedExamples: UserSpecifiedEndpointExample.Raw[];
        autogeneratedExamples: AutogeneratedEndpointExample.Raw[];
    }
}
