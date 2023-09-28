param(
    [String]$scopeName,
    [String]$subnet,
    [String]$mask,
    [String]$router,
    [String]$dnsServers,
    [String]$domain,
    [String]$startRange,
    [String]$endRange,
    [String]$startExclusionRange,
    [String]$endExclusionRange
)

Add-DhcpServerv4Scope `
    -name $scopeName `
    -StartRange $startRange `
    -EndRange $endRange `
    -SubnetMask $mask `
    -State Active

Add-DhcpServerv4ExclusionRange `
    -ScopeID $subnet `
    -StartRange $startExclusionRange `
    -EndRange $endExclusionRange

Set-DhcpServerv4OptionValue `
    -ScopeId $subnet `
    -DnsServer $dnsServers `
    -Router $router `
    -DnsDomain $domain
