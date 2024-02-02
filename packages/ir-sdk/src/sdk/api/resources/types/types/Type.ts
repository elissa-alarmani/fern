/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernIr from "../../..";

export type Type =
    | FernIr.Type.Alias
    | FernIr.Type.Enum
    | FernIr.Type.Object_
    | FernIr.Type.Union
    | FernIr.Type.UndiscriminatedUnion;

export declare namespace Type {
    interface Alias extends FernIr.AliasTypeDeclaration, _Utils {
        type: "alias";
    }

    interface Enum extends FernIr.EnumTypeDeclaration, _Utils {
        type: "enum";
    }

    interface Object_ extends FernIr.ObjectTypeDeclaration, _Utils {
        type: "object";
    }

    interface Union extends FernIr.UnionTypeDeclaration, _Utils {
        type: "union";
    }

    interface UndiscriminatedUnion extends FernIr.UndiscriminatedUnionTypeDeclaration, _Utils {
        type: "undiscriminatedUnion";
    }

    interface _Utils {
        _visit: <_Result>(visitor: FernIr.Type._Visitor<_Result>) => _Result;
    }

    interface _Visitor<_Result> {
        alias: (value: FernIr.AliasTypeDeclaration) => _Result;
        enum: (value: FernIr.EnumTypeDeclaration) => _Result;
        object: (value: FernIr.ObjectTypeDeclaration) => _Result;
        union: (value: FernIr.UnionTypeDeclaration) => _Result;
        undiscriminatedUnion: (value: FernIr.UndiscriminatedUnionTypeDeclaration) => _Result;
        _other: (value: { type: string }) => _Result;
    }
}

export const Type = {
    alias: (value: FernIr.AliasTypeDeclaration): FernIr.Type.Alias => {
        return {
            ...value,
            type: "alias",
            _visit: function <_Result>(this: FernIr.Type.Alias, visitor: FernIr.Type._Visitor<_Result>) {
                return FernIr.Type._visit(this, visitor);
            },
        };
    },

    enum: (value: FernIr.EnumTypeDeclaration): FernIr.Type.Enum => {
        return {
            ...value,
            type: "enum",
            _visit: function <_Result>(this: FernIr.Type.Enum, visitor: FernIr.Type._Visitor<_Result>) {
                return FernIr.Type._visit(this, visitor);
            },
        };
    },

    object: (value: FernIr.ObjectTypeDeclaration): FernIr.Type.Object_ => {
        return {
            ...value,
            type: "object",
            _visit: function <_Result>(this: FernIr.Type.Object_, visitor: FernIr.Type._Visitor<_Result>) {
                return FernIr.Type._visit(this, visitor);
            },
        };
    },

    union: (value: FernIr.UnionTypeDeclaration): FernIr.Type.Union => {
        return {
            ...value,
            type: "union",
            _visit: function <_Result>(this: FernIr.Type.Union, visitor: FernIr.Type._Visitor<_Result>) {
                return FernIr.Type._visit(this, visitor);
            },
        };
    },

    undiscriminatedUnion: (value: FernIr.UndiscriminatedUnionTypeDeclaration): FernIr.Type.UndiscriminatedUnion => {
        return {
            ...value,
            type: "undiscriminatedUnion",
            _visit: function <_Result>(this: FernIr.Type.UndiscriminatedUnion, visitor: FernIr.Type._Visitor<_Result>) {
                return FernIr.Type._visit(this, visitor);
            },
        };
    },

    _visit: <_Result>(value: FernIr.Type, visitor: FernIr.Type._Visitor<_Result>): _Result => {
        switch (value.type) {
            case "alias":
                return visitor.alias(value);
            case "enum":
                return visitor.enum(value);
            case "object":
                return visitor.object(value);
            case "union":
                return visitor.union(value);
            case "undiscriminatedUnion":
                return visitor.undiscriminatedUnion(value);
            default:
                return visitor._other(value as any);
        }
    },
} as const;
