/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   q01-explorer-guild.swift                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/10/30 17:10:10 by cbaek             #+#    #+#             */
/*   Updated: 2020/10/30 17:19:16 by cbaek            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

var inputCount = Int(readLine()!)!
var inputData = (readLine()!).split(separator: " ").map { Int($0)! }

var result = 0
var count = 0

for index in 0..<inputData.count {
	count += 1
	if count >= inputData[index] {
		result += 1
		count = 0
	}
}

print(result)
