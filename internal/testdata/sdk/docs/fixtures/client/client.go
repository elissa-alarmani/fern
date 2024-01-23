// This file was auto-generated by Fern from our API Definition.

package client

import (
	core "github.com/fern-api/fern-go/internal/testdata/sdk/docs/fixtures/core"
	option "github.com/fern-api/fern-go/internal/testdata/sdk/docs/fixtures/option"
	user "github.com/fern-api/fern-go/internal/testdata/sdk/docs/fixtures/user"
	http "net/http"
)

type Client struct {
	baseURL string
	caller  *core.Caller
	header  http.Header

	User *user.Client
}

func NewClient(opts ...option.RequestOption) *Client {
	options := core.NewRequestOptions(opts...)
	return &Client{
		baseURL: options.BaseURL,
		caller:  core.NewCaller(options.HTTPClient),
		header:  options.ToHeader(),
		User:    user.NewClient(opts...),
	}
}
