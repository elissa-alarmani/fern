// This file was auto-generated by Fern from our API Definition.

package user

import (
	context "context"
	base64 "encoding/base64"
	fmt "fmt"
	fixtures "github.com/fern-api/fern-go/internal/testdata/sdk/headers/fixtures"
	core "github.com/fern-api/fern-go/internal/testdata/sdk/headers/fixtures/core"
	http "net/http"
	time "time"
)

type Client struct {
	baseURL string
	caller  *core.Caller
	header  http.Header
}

func NewClient(opts ...core.ClientOption) *Client {
	options := core.NewClientOptions()
	for _, opt := range opts {
		opt(options)
	}
	return &Client{
		baseURL: options.BaseURL,
		caller:  core.NewCaller(options.HTTPClient),
		header:  options.ToHeader(),
	}
}

func (c *Client) SetName(ctx context.Context, userId string, request *fixtures.SetNameRequest) (string, error) {
	baseURL := ""
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	endpointURL := fmt.Sprintf(baseURL+"/"+"users/%v/set-name", userId)

	headers := c.header.Clone()
	headers.Add("X-Endpoint-Header", fmt.Sprintf("%v", request.XEndpointHeader))
	headers.Add("X-Endpoint-ID-Header", fmt.Sprintf("%v", request.XEndpointIdHeader))
	headers.Add("X-Endpoint-Date-Header", fmt.Sprintf("%v", request.XEndpointDateHeader.Format("2006-01-02")))
	headers.Add("X-Endpoint-Datetime-Header", fmt.Sprintf("%v", request.XEndpointDatetimeHeader.Format(time.RFC3339)))
	headers.Add("X-Endpoint-Bytes-Header", fmt.Sprintf("%v", base64.StdEncoding.EncodeToString(request.XEndpointBytesHeader)))
	if request.XEndpointOptionalHeader != nil {
		headers.Add("X-Endpoint-Optional-Header", fmt.Sprintf("%v", *request.XEndpointOptionalHeader))
	}
	if request.XEndpointOptionalIdHeader != nil {
		headers.Add("X-Endpoint-Optional-ID-Header", fmt.Sprintf("%v", *request.XEndpointOptionalIdHeader))
	}
	if request.XEndpointOptionalDateHeader != nil {
		headers.Add("X-Endpoint-Optional-Date-Header", fmt.Sprintf("%v", request.XEndpointOptionalDateHeader.Format("2006-01-02")))
	}
	if request.XEndpointOptionalDatetimeHeader != nil {
		headers.Add("X-Endpoint-Optional-Datetime-Header", fmt.Sprintf("%v", request.XEndpointOptionalDatetimeHeader.Format(time.RFC3339)))
	}
	if request.XEndpointOptionalBytesHeader != nil {
		headers.Add("X-Endpoint-Optional-Bytes-Header", fmt.Sprintf("%v", base64.StdEncoding.EncodeToString(*request.XEndpointOptionalBytesHeader)))
	}
	headers.Add("X-Endpoint-Fern-Header", fmt.Sprintf("%v", "fern"))

	var response string
	if err := c.caller.Call(
		ctx,
		&core.CallParams{
			URL:      endpointURL,
			Method:   http.MethodPost,
			Headers:  headers,
			Response: &response,
		},
	); err != nil {
		return "", err
	}
	return response, nil
}

func (c *Client) UpdateName(ctx context.Context, userId string, request *fixtures.UpdateNameRequest) (string, error) {
	baseURL := ""
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	endpointURL := fmt.Sprintf(baseURL+"/"+"users/%v/update-name", userId)

	headers := c.header.Clone()
	headers.Add("X-Endpoint-Header", fmt.Sprintf("%v", request.XEndpointHeader))
	headers.Add("Idempotency-Key", fmt.Sprintf("%v", request.IdempotencyKey))

	var response string
	if err := c.caller.Call(
		ctx,
		&core.CallParams{
			URL:      endpointURL,
			Method:   http.MethodPut,
			Headers:  headers,
			Response: &response,
		},
	); err != nil {
		return "", err
	}
	return response, nil
}
