/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   q02-multiply-or-sum.swift                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/10/31 15:43:52 by cbaek             #+#    #+#             */
/*   Updated: 2020/10/31 15:56:56 by cbaek            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

import Foundation

var data = readLine()!
var result = 0

for index in data.indices {
	let item = Int(String(data[index]))!
	if result == 0 {
		result += item
	} else {
		if result <= 1 || item <= 1 {
			result += item
		} else {
			result *= item
		}
	}
}

print(result)
