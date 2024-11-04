package example

import (
    client "github.com/grpc-proto-exhaustive/fern/client"
    option "github.com/grpc-proto-exhaustive/fern/option"
    context "context"
    fern "github.com/grpc-proto-exhaustive/fern"
)

func do() () {
    client := client.NewClient(
        option.WithApiKey(
            "<value>",
        ),
    )
    client.Dataservice.Update(
        context.TODO(),
        &fern.UpdateRequest{
            Id: "id",
        },
    )
}
