/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernIr from "../../../../api";
import * as core from "../../../../core";

export const FileUploadRequest: core.serialization.ObjectSchema<
    serializers.FileUploadRequest.Raw,
    FernIr.FileUploadRequest
> = core.serialization.objectWithoutOptionalProperties({
    name: core.serialization.lazyObject(async () => (await import("../../..")).Name),
    properties: core.serialization.list(
        core.serialization.lazy(async () => (await import("../../..")).FileUploadRequestProperty)
    ),
});

export declare namespace FileUploadRequest {
    interface Raw {
        name: serializers.Name.Raw;
        properties: serializers.FileUploadRequestProperty.Raw[];
    }
}
