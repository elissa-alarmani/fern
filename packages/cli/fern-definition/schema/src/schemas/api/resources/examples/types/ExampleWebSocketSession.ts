/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernDefinition from "../../../index";

export interface ExampleWebSocketSession extends FernDefinition.WithName, FernDefinition.WithDocs {
    "path-parameters"?: Record<string, FernDefinition.ExampleTypeReferenceSchema | undefined>;
    "query-parameters"?: Record<string, FernDefinition.ExampleTypeReferenceSchema | undefined>;
    headers?: Record<string, FernDefinition.ExampleTypeReferenceSchema | undefined>;
    message: FernDefinition.ExampleWebSocketMessage[];
}
