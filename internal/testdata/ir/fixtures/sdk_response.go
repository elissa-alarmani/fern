// Generated by Fern. Do not edit.

package ir

import (
	json "encoding/json"
	fmt "fmt"
)

type SdkResponse struct {
	Type           string
	Json           *JsonResponse
	Streaming      *StreamingResponse
	MaybeStreaming *MaybeStreamingResponse
	FileDownload   *FileDownloadResponse
}

func (s *SdkResponse) UnmarshalJSON(data []byte) error {
	var unmarshaler struct {
		Type string `json:"type"`
	}
	if err := json.Unmarshal(data, &unmarshaler); err != nil {
		return err
	}
	s.Type = unmarshaler.Type
	switch unmarshaler.Type {
	case "json":
		value := new(JsonResponse)
		if err := json.Unmarshal(data, &value); err != nil {
			return err
		}
		s.Json = value
	case "streaming":
		value := new(StreamingResponse)
		if err := json.Unmarshal(data, &value); err != nil {
			return err
		}
		s.Streaming = value
	case "maybeStreaming":
		value := new(MaybeStreamingResponse)
		if err := json.Unmarshal(data, &value); err != nil {
			return err
		}
		s.MaybeStreaming = value
	case "fileDownload":
		value := new(FileDownloadResponse)
		if err := json.Unmarshal(data, &value); err != nil {
			return err
		}
		s.FileDownload = value
	}
	return nil
}

func (s SdkResponse) MarshalJSON() ([]byte, error) {
	switch s.Type {
	default:
		return nil, fmt.Errorf("invalid type %s in %T", s.Type, s)
	case "json":
		var marshaler = struct {
			Type string `json:"type"`
			*JsonResponse
		}{
			Type:         s.Type,
			JsonResponse: s.Json,
		}
		return json.Marshal(marshaler)
	case "streaming":
		var marshaler = struct {
			Type string `json:"type"`
			*StreamingResponse
		}{
			Type:              s.Type,
			StreamingResponse: s.Streaming,
		}
		return json.Marshal(marshaler)
	case "maybeStreaming":
		var marshaler = struct {
			Type string `json:"type"`
			*MaybeStreamingResponse
		}{
			Type:                   s.Type,
			MaybeStreamingResponse: s.MaybeStreaming,
		}
		return json.Marshal(marshaler)
	case "fileDownload":
		var marshaler = struct {
			Type string `json:"type"`
			*FileDownloadResponse
		}{
			Type:                 s.Type,
			FileDownloadResponse: s.FileDownload,
		}
		return json.Marshal(marshaler)
	}
}

type SdkResponseVisitor interface {
	VisitJson(*JsonResponse) error
	VisitStreaming(*StreamingResponse) error
	VisitMaybeStreaming(*MaybeStreamingResponse) error
	VisitFileDownload(*FileDownloadResponse) error
}

func (s *SdkResponse) Accept(v SdkResponseVisitor) error {
	switch s.Type {
	default:
		return fmt.Errorf("invalid type %s in %T", s.Type, s)
	case "json":
		return v.VisitJson(s.Json)
	case "streaming":
		return v.VisitStreaming(s.Streaming)
	case "maybeStreaming":
		return v.VisitMaybeStreaming(s.MaybeStreaming)
	case "fileDownload":
		return v.VisitFileDownload(s.FileDownload)
	}
}
