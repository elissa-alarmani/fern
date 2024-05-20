/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernOpenapiIr from "../../../../api";
import * as core from "../../../../core";

export const IntSchema: core.serialization.ObjectSchema<serializers.IntSchema.Raw, FernOpenapiIr.IntSchema> =
    core.serialization.objectWithoutOptionalProperties({
        default: core.serialization.number().optional(),
        minimum: core.serialization.number().optional(),
        maximum: core.serialization.number().optional(),
        exclusiveMinimum: core.serialization.boolean().optional(),
        exclusiveMaximum: core.serialization.boolean().optional(),
        multipleOf: core.serialization.number().optional(),
    });

export declare namespace IntSchema {
    interface Raw {
        default?: number | null;
        minimum?: number | null;
        maximum?: number | null;
        exclusiveMinimum?: boolean | null;
        exclusiveMaximum?: boolean | null;
        multipleOf?: number | null;
    }
}
