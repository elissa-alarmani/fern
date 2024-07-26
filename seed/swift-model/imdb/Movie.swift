//
//  Movie.swift
//
//
//  This file was auto-generated by Fern
//

import Foundation

public struct Movie: Codable {

    enum CodingKeys: String, CodingKey {
        case id = "id"
        case title = "title"
        case rating = "rating"
    }

    public let id: MovieId
    public let title: String

    /// The rating scale is one to five stars
    public let rating: Double

    public init(id: MovieId, title: String, rating: Double) {
        self.id = id
        self.title = title
        self.rating = rating
    }

}
