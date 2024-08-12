/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernIr from "../../../../api/index";
import * as core from "../../../../core";
import { AliasTypeDeclaration } from "./AliasTypeDeclaration";
import { EnumTypeDeclaration } from "./EnumTypeDeclaration";
import { ObjectTypeDeclaration } from "./ObjectTypeDeclaration";
import { UnionTypeDeclaration } from "./UnionTypeDeclaration";
import { UndiscriminatedUnionTypeDeclaration } from "./UndiscriminatedUnionTypeDeclaration";

export const Type: core.serialization.Schema<serializers.Type.Raw, FernIr.Type> = core.serialization
    .union(core.serialization.discriminant("type", "_type"), {
        alias: AliasTypeDeclaration,
        enum: EnumTypeDeclaration,
        object: ObjectTypeDeclaration,
        union: UnionTypeDeclaration,
        undiscriminatedUnion: UndiscriminatedUnionTypeDeclaration,
    })
    .transform<FernIr.Type>({
        transform: (value) => {
            switch (value.type) {
                case "alias":
                    return FernIr.Type.alias(value);
                case "enum":
                    return FernIr.Type.enum(value);
                case "object":
                    return FernIr.Type.object(value);
                case "union":
                    return FernIr.Type.union(value);
                case "undiscriminatedUnion":
                    return FernIr.Type.undiscriminatedUnion(value);
                default:
                    return value as FernIr.Type;
            }
        },
        untransform: ({ _visit, ...value }) => value as any,
    });

export declare namespace Type {
    type Raw = Type.Alias | Type.Enum | Type.Object | Type.Union | Type.UndiscriminatedUnion;

    interface Alias extends AliasTypeDeclaration.Raw {
        _type: "alias";
    }

    interface Enum extends EnumTypeDeclaration.Raw {
        _type: "enum";
    }

    interface Object extends ObjectTypeDeclaration.Raw {
        _type: "object";
    }

    interface Union extends UnionTypeDeclaration.Raw {
        _type: "union";
    }

    interface UndiscriminatedUnion extends UndiscriminatedUnionTypeDeclaration.Raw {
        _type: "undiscriminatedUnion";
    }
}
