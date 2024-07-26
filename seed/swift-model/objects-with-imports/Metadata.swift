//
//  Metadata.swift
//
//
//  This file was auto-generated by Fern
//

import Foundation

public struct Metadata: Codable {

    enum CodingKeys: String, CodingKey {
        case id = "id"
        case data = "data"
    }

    public let id: String
    public let data: [String: String]?

    public init(id: String, data: [String: String]? = nil) {
        self.id = id
        self.data = data
    }

}
