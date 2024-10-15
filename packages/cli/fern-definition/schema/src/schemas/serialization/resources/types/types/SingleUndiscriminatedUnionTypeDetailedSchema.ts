/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernDefinition from "../../../../api/index";
import * as core from "../../../../core";
import { WithDocs } from "../../commons/types/WithDocs";
import { WithDisplayName } from "../../commons/types/WithDisplayName";

export const SingleUndiscriminatedUnionTypeDetailedSchema: core.serialization.ObjectSchema<
    serializers.SingleUndiscriminatedUnionTypeDetailedSchema.Raw,
    FernDefinition.SingleUndiscriminatedUnionTypeDetailedSchema
> = core.serialization
    .object({
        type: core.serialization.string(),
    })
    .extend(WithDocs)
    .extend(WithDisplayName);

export declare namespace SingleUndiscriminatedUnionTypeDetailedSchema {
    interface Raw extends WithDocs.Raw, WithDisplayName.Raw {
        type: string;
    }
}
