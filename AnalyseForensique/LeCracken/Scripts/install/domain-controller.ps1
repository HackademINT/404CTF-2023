param(
    [String]$domain,
    [String]$nbName,
    [String]$safeModePassword
)

$safeModeAdminstratorPassword = ConvertTo-SecureString $safeModePassword -AsPlainText -Force

Install-WindowsFeature AD-Domain-Services,RSAT-AD-AdminCenter,RSAT-ADDS-Tools
Import-Module ADDSDeployment

Install-ADDSForest `
    -InstallDns `
    -CreateDnsDelegation:$false `
    -ForestMode 'WinThreshold' `
    -DomainMode 'WinThreshold' `
    -DomainName $domain `
    -DomainNetbiosName $nbName `
    -SafeModeAdministratorPassword $safeModeAdminstratorPassword `
    -NoRebootOnCompletion `
    -Force
