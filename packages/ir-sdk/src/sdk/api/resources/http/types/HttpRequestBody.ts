/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernIr from "../../..";

export type HttpRequestBody =
    | FernIr.HttpRequestBody.InlinedRequestBody
    | FernIr.HttpRequestBody.Reference
    | FernIr.HttpRequestBody.FileUpload
    | FernIr.HttpRequestBody.Bytes;

export declare namespace HttpRequestBody {
    interface InlinedRequestBody extends FernIr.InlinedRequestBody, _Utils {
        type: "inlinedRequestBody";
    }

    interface Reference extends FernIr.HttpRequestBodyReference, _Utils {
        type: "reference";
    }

    interface FileUpload extends FernIr.FileUploadRequest, _Utils {
        type: "fileUpload";
    }

    interface Bytes extends FernIr.BytesRequest, _Utils {
        type: "bytes";
    }

    interface _Utils {
        _visit: <_Result>(visitor: FernIr.HttpRequestBody._Visitor<_Result>) => _Result;
    }

    interface _Visitor<_Result> {
        inlinedRequestBody: (value: FernIr.InlinedRequestBody) => _Result;
        reference: (value: FernIr.HttpRequestBodyReference) => _Result;
        fileUpload: (value: FernIr.FileUploadRequest) => _Result;
        bytes: (value: FernIr.BytesRequest) => _Result;
        _other: (value: { type: string }) => _Result;
    }
}

export const HttpRequestBody = {
    inlinedRequestBody: (value: FernIr.InlinedRequestBody): FernIr.HttpRequestBody.InlinedRequestBody => {
        return {
            ...value,
            type: "inlinedRequestBody",
            _visit: function <_Result>(
                this: FernIr.HttpRequestBody.InlinedRequestBody,
                visitor: FernIr.HttpRequestBody._Visitor<_Result>
            ) {
                return FernIr.HttpRequestBody._visit(this, visitor);
            },
        };
    },

    reference: (value: FernIr.HttpRequestBodyReference): FernIr.HttpRequestBody.Reference => {
        return {
            ...value,
            type: "reference",
            _visit: function <_Result>(
                this: FernIr.HttpRequestBody.Reference,
                visitor: FernIr.HttpRequestBody._Visitor<_Result>
            ) {
                return FernIr.HttpRequestBody._visit(this, visitor);
            },
        };
    },

    fileUpload: (value: FernIr.FileUploadRequest): FernIr.HttpRequestBody.FileUpload => {
        return {
            ...value,
            type: "fileUpload",
            _visit: function <_Result>(
                this: FernIr.HttpRequestBody.FileUpload,
                visitor: FernIr.HttpRequestBody._Visitor<_Result>
            ) {
                return FernIr.HttpRequestBody._visit(this, visitor);
            },
        };
    },

    bytes: (value: FernIr.BytesRequest): FernIr.HttpRequestBody.Bytes => {
        return {
            ...value,
            type: "bytes",
            _visit: function <_Result>(
                this: FernIr.HttpRequestBody.Bytes,
                visitor: FernIr.HttpRequestBody._Visitor<_Result>
            ) {
                return FernIr.HttpRequestBody._visit(this, visitor);
            },
        };
    },

    _visit: <_Result>(value: FernIr.HttpRequestBody, visitor: FernIr.HttpRequestBody._Visitor<_Result>): _Result => {
        switch (value.type) {
            case "inlinedRequestBody":
                return visitor.inlinedRequestBody(value);
            case "reference":
                return visitor.reference(value);
            case "fileUpload":
                return visitor.fileUpload(value);
            case "bytes":
                return visitor.bytes(value);
            default:
                return visitor._other(value as any);
        }
    },
} as const;
