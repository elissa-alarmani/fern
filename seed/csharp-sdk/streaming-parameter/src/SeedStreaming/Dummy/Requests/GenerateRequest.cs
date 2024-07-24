using System.Text.Json.Serialization;

#nullable enable

namespace SeedStreaming;

public record GenerateRequest
{
    [JsonPropertyName("stream")]
    public required bool Stream { get; init; }

    [JsonPropertyName("num_events")]
    public required int NumEvents { get; init; }
}
