/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernIr from "../../../../api";
import * as core from "../../../../core";

export const SdkRequest: core.serialization.ObjectSchema<serializers.SdkRequest.Raw, FernIr.SdkRequest> =
    core.serialization.objectWithoutOptionalProperties({
        requestParameterName: core.serialization.lazyObject(async () => (await import("../../..")).Name),
        shape: core.serialization.lazy(async () => (await import("../../..")).SdkRequestShape),
    });

export declare namespace SdkRequest {
    interface Raw {
        requestParameterName: serializers.Name.Raw;
        shape: serializers.SdkRequestShape.Raw;
    }
}
