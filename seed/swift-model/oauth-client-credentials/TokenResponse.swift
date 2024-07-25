//
//  TokenResponse.swift
//
//
//  This file was auto-generated by Fern
//

import Foundation

public struct TokenResponse: Codable {

    enum CodingKeys: String, CodingKey {
        case accessToken = "access_token"
        case expiresIn = "expires_in"
        case refreshToken = "refresh_token"
    }

    public let accessToken: String
    public let expiresIn: Int
    public let refreshToken: String?

}
