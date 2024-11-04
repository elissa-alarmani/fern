/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../../index";
import * as FernIr from "../../../../../../api/index";
import * as core from "../../../../../../core";
import { FileContent } from "./FileContent";

export const FileValue: core.serialization.ObjectSchema<serializers.dynamic.FileValue.Raw, FernIr.dynamic.FileValue> =
    core.serialization.objectWithoutOptionalProperties({
        content: FileContent,
        contentType: core.serialization.string().optional(),
    });

export declare namespace FileValue {
    interface Raw {
        content: FileContent.Raw;
        contentType?: string | null;
    }
}
