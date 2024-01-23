// This file was auto-generated by Fern from our API Definition.

package client

import (
	core "github.com/acme/acme-go/core"
	file "github.com/acme/acme-go/file"
	option "github.com/acme/acme-go/option"
	http "net/http"
)

type Client struct {
	baseURL string
	caller  *core.Caller
	header  http.Header

	File *file.Client
}

func NewClient(opts ...option.RequestOption) *Client {
	options := core.NewRequestOptions(opts...)
	return &Client{
		baseURL: options.BaseURL,
		caller:  core.NewCaller(options.HTTPClient),
		header:  options.ToHeader(),
		File:    file.NewClient(opts...),
	}
}
