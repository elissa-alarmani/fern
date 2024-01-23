// This file was auto-generated by Fern from our API Definition.

package client

import (
	core "github.com/fern-api/stream-go/v2/core"
	dummy "github.com/fern-api/stream-go/v2/dummy"
	option "github.com/fern-api/stream-go/v2/option"
	http "net/http"
)

type Client struct {
	baseURL string
	caller  *core.Caller
	header  http.Header

	Dummy *dummy.Client
}

func NewClient(opts ...option.RequestOption) *Client {
	options := core.NewRequestOptions(opts...)
	return &Client{
		baseURL: options.BaseURL,
		caller:  core.NewCaller(options.HTTPClient),
		header:  options.ToHeader(),
		Dummy:   dummy.NewClient(opts...),
	}
}
