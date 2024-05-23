using System.Text.Json.Serialization;
using SeedTrace;

namespace SeedTrace;

public class GetDefaultStarterFilesRequest
{
    [JsonPropertyName("inputParams")]
    public List<VariableTypeAndName> InputParams { get; init; }

    [JsonPropertyName("outputType")]
    public VariableType OutputType { get; init; }

    /// <summary>
    /// The name of the `method` that the student has to complete.
    /// The method name cannot include the following characters:
    ///   - Greater Than `>`
    ///   - Less Than `<``
    ///   - Equals `=`
    ///   - Period `.`
    ///
    /// </summary>
    [JsonPropertyName("methodName")]
    public string MethodName { get; init; }
}
