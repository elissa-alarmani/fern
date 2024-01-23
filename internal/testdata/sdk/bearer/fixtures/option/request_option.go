// This file was auto-generated by Fern from our API Definition.

package option

import (
	core "github.com/fern-api/fern-go/internal/testdata/sdk/bearer/fixtures/core"
	http "net/http"
)

// RequestOption adapts the behavior of an indivdual request.
type RequestOption = core.RequestOption

// WithBaseURL sets the base URL, overriding the default
// environment, if any.
func WithBaseURL(baseURL string) *core.BaseURLOption {
	return &core.BaseURLOption{
		BaseURL: baseURL,
	}
}

// WithHTTPClient uses the given HTTPClient to issue the request.
func WithHTTPClient(httpClient core.HTTPClient) *core.HTTPClientOption {
	return &core.HTTPClientOption{
		HTTPClient: httpClient,
	}
}

// WithHTTPHeader adds the given http.Header to the request.
func WithHTTPHeader(httpHeader http.Header) *core.HTTPHeaderOption {
	return &core.HTTPHeaderOption{
		// Clone the headers so they can't be modified after the option call.
		HTTPHeader: httpHeader.Clone(),
	}
}

// WithToken sets the 'Authorization: Bearer <token>' request header.
func WithToken(token string) *core.TokenOption {
	return &core.TokenOption{
		Token: token,
	}
}
