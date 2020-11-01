/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   q03-reverse-string.swift                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/11/01 22:07:09 by cbaek             #+#    #+#             */
/*   Updated: 2020/11/01 22:16:13 by cbaek            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// Q03 문자열 뒤집기 p.313.

var inputData = readLine()!
var seperateByOne = inputData.split(separator: "1").count
var seperateByZero = inputData.split(separator: "0").count

print(seperateByOne < seperateByZero ? seperateByOne : seperateByZero)
