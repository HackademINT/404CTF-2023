param(
    [String]$name,
    [String]$login,
    [String]$password,
    [String]$domainAdmin
)

$safePassword = ConvertTo-SecureString $password -AsPlainText -Force

New-ADUser `
    -Name $name `
    -UserPrincipalName $login `
    -Accountpassword $safePassword `
    -Enabled $true

if ( $domainAdmin -eq "true" )
{
    Add-ADGroupMember -Identity "Domain Admins" -Members $name
}
