using System.Text.Json.Serialization;
using SeedTrace;

namespace SeedTrace;

public class RecordingResponseNotification
{
    [JsonPropertyName("submissionId")]
    public Guid SubmissionId { get; init; }

    [JsonPropertyName("testCaseId")]
    public List<string?> TestCaseId { get; init; }

    [JsonPropertyName("lineNumber")]
    public int LineNumber { get; init; }

    [JsonPropertyName("lightweightStackInfo")]
    public LightweightStackframeInformation LightweightStackInfo { get; init; }

    [JsonPropertyName("tracedFile")]
    public List<TracedFile?> TracedFile { get; init; }
}
