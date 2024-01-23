// This file was auto-generated by Fern from our API Definition.

package client

import (
	core "github.com/literal/fern/core"
	literal "github.com/literal/fern/literal"
	option "github.com/literal/fern/option"
	http "net/http"
)

type Client struct {
	baseURL string
	caller  *core.Caller
	header  http.Header

	Literal *literal.Client
}

func NewClient(opts ...option.RequestOption) *Client {
	options := core.NewRequestOptions(opts...)
	return &Client{
		baseURL: options.BaseURL,
		caller:  core.NewCaller(options.HTTPClient),
		header:  options.ToHeader(),
		Literal: literal.NewClient(opts...),
	}
}
