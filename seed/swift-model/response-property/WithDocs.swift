//
//  WithDocs.swift
//
//
//  This file was auto-generated by Fern
//

import Foundation

public struct WithDocs: Codable {

    enum CodingKeys: String, CodingKey {
        case docs = "docs"
    }

    public let docs: String

    public init(docs: String) {
        self.docs = docs
    }

}
