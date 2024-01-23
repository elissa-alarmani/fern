// This file was auto-generated by Fern from our API Definition.

package user

import (
	sdk "acme.io/sdk"
	core "acme.io/sdk/core"
	option "acme.io/sdk/option"
	context "context"
	fmt "fmt"
	http "net/http"
	url "net/url"
)

type Client struct {
	baseURL string
	caller  *core.Caller
	header  http.Header
}

func NewClient(opts ...option.RequestOption) *Client {
	options := core.NewRequestOptions(opts...)
	return &Client{
		baseURL: options.BaseURL,
		caller:  core.NewCaller(options.HTTPClient),
		header:  options.ToHeader(),
	}
}

func (c *Client) SetName(ctx context.Context, userId string, request string) (string, error) {
	baseURL := ""
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	endpointURL := fmt.Sprintf(baseURL+"/"+"users/%v/set-name", userId)

	var response string
	if err := c.caller.Call(
		ctx,
		&core.CallParams{
			URL:      endpointURL,
			Method:   http.MethodPost,
			Headers:  c.header,
			Request:  request,
			Response: &response,
		},
	); err != nil {
		return "", err
	}
	return response, nil
}

func (c *Client) SetNameV2(ctx context.Context, userId string, request *sdk.SetNameRequest) (string, error) {
	baseURL := ""
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	endpointURL := fmt.Sprintf(baseURL+"/"+"users/%v/set-name-v2", userId)

	var response string
	if err := c.caller.Call(
		ctx,
		&core.CallParams{
			URL:      endpointURL,
			Method:   http.MethodPost,
			Headers:  c.header,
			Request:  request,
			Response: &response,
		},
	); err != nil {
		return "", err
	}
	return response, nil
}

func (c *Client) SetNameV3(ctx context.Context, userId string, request *sdk.SetNameRequestV3) (*sdk.SetNameRequestV3Body, error) {
	baseURL := ""
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	endpointURL := fmt.Sprintf(baseURL+"/"+"users/%v/set-name-v3", userId)

	headers := c.header.Clone()
	headers.Add("X-Endpoint-Header", fmt.Sprintf("%v", request.XEndpointHeader))

	var response *sdk.SetNameRequestV3Body
	if err := c.caller.Call(
		ctx,
		&core.CallParams{
			URL:      endpointURL,
			Method:   http.MethodPost,
			Headers:  headers,
			Request:  request,
			Response: &response,
		},
	); err != nil {
		return nil, err
	}
	return response, nil
}

func (c *Client) SetNameV3Optional(ctx context.Context, userId string, request *sdk.SetNameRequestV3Optional) (*sdk.SetNameRequestV3Body, error) {
	baseURL := ""
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	endpointURL := fmt.Sprintf(baseURL+"/"+"users/%v/set-name-v3-optional", userId)

	headers := c.header.Clone()
	headers.Add("X-Endpoint-Header", fmt.Sprintf("%v", request.XEndpointHeader))

	var response *sdk.SetNameRequestV3Body
	if err := c.caller.Call(
		ctx,
		&core.CallParams{
			URL:                endpointURL,
			Method:             http.MethodPost,
			Headers:            headers,
			Request:            request,
			Response:           &response,
			ResponseIsOptional: true,
		},
	); err != nil {
		return nil, err
	}
	return response, nil
}

func (c *Client) SetNameV4(ctx context.Context, userId string, request *sdk.SetNameRequestV4) (string, error) {
	baseURL := ""
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	endpointURL := fmt.Sprintf(baseURL+"/"+"users/%v/set-name-v4", userId)

	headers := c.header.Clone()
	headers.Add("X-Endpoint-Header", fmt.Sprintf("%v", request.XEndpointHeader))

	var response string
	if err := c.caller.Call(
		ctx,
		&core.CallParams{
			URL:      endpointURL,
			Method:   http.MethodPost,
			Headers:  headers,
			Request:  request,
			Response: &response,
		},
	); err != nil {
		return "", err
	}
	return response, nil
}

func (c *Client) SetNameV5(ctx context.Context, userId string, request *sdk.SetNameRequestV5) (string, error) {
	baseURL := ""
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	endpointURL := fmt.Sprintf(baseURL+"/"+"users/%v/set-name-v5", userId)

	headers := c.header.Clone()
	headers.Add("X-Endpoint-Header", fmt.Sprintf("%v", request.XEndpointHeader))

	var response string
	if err := c.caller.Call(
		ctx,
		&core.CallParams{
			URL:      endpointURL,
			Method:   http.MethodPost,
			Headers:  headers,
			Request:  request,
			Response: &response,
		},
	); err != nil {
		return "", err
	}
	return response, nil
}

func (c *Client) Update(ctx context.Context, userId string, request *sdk.UpdateRequest) (string, error) {
	baseURL := ""
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	endpointURL := fmt.Sprintf(baseURL+"/"+"users/%v/update", userId)

	queryParams := make(url.Values)
	queryParams.Add("tag", fmt.Sprintf("%v", request.Tag))
	if request.Extra != nil {
		queryParams.Add("extra", fmt.Sprintf("%v", *request.Extra))
	}
	if len(queryParams) > 0 {
		endpointURL += "?" + queryParams.Encode()
	}

	var response string
	if err := c.caller.Call(
		ctx,
		&core.CallParams{
			URL:      endpointURL,
			Method:   http.MethodPost,
			Headers:  c.header,
			Request:  request,
			Response: &response,
		},
	); err != nil {
		return "", err
	}
	return response, nil
}
