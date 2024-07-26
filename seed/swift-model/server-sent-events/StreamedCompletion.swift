//
//  StreamedCompletion.swift
//
//
//  This file was auto-generated by Fern
//

import Foundation

public struct StreamedCompletion: Codable {

    enum CodingKeys: String, CodingKey {
        case delta = "delta"
        case tokens = "tokens"
    }

    public let delta: String
    public let tokens: Int?

    public init(delta: String, tokens: Int? = nil) {
        self.delta = delta
        self.tokens = tokens
    }

}
