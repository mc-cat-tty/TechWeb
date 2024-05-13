# Introduzione
>Cloud-computing: forma di 

# Storia
Inventato dal ricercatore McCarthy nel 1961 (MIT):
>Computing may someday be organized as public utility

Nel 2006 Jeff Bezos propone:
>Let us use or spare resources for making profit by offering them as services to the public

NIST - National Institute of Standards and Technology - fornisce una definizione, 5 anni dopo la nascita da parte di iniziativa privata:
>Cloud computing is a **model** for enabling **ubiquitous, convenient, on-demand** network access to a **shared pool** (*condivisione*) of **configurable computing resources** (*espansione delle risorse*) that can be rapidly provisioned and released with minimal mgmt effort or service provider interaction. This Cloud model promotes:
>- **availability**: high availability, etc.
>- **elasticity**: resources scalability
>- **security**

#Vedi traffico elastico, variabile nel tempo, come il traffico stradale a fisarmonica

# Caratteristiche
>SLA - **Service Level Agreement** -: contratto stipulato con il cloud provider, in cui vengono definite le garanzie offerte da

## Attori
- **provider**: fornisce il servizio
- **costumer**: organizzazione che paga e sfrutta il servizio del provider
- **final user**: singolo utente che fa uso del servizio offerto dal customer; usa indirettamente le infrastrutture del provider
## Paradigmi
>On Premise: controllo totale dalle risorse hw in su
>Hosting provider: affitta hw su cui eseguire VM
>IaaS - Infrastructure as a Service: totale controllo sul SO (Amazon EC2)
>PaaS - Platform as a Service: controllo sul middleware (venv/container)
>SaaS - Software as a Service: controllo amministrativo sul software (Gmail for organizations)

I 4 paradigmi differiscono nella quantità dello stack gestita dal *customer*; la parte restante è gestita dal *provider*:

| Paradigm   | Net | Storage | Server | Virt | OS  | Middleware | Runtime | Data | App |
| ---------- | --- | ------- | ------ | ---- | --- | ---------- | ------- | ---- | --- |
| On Premise | v   | v       | v      | v    | v   | v          | v       | v    | v   |
| IaaS       | x   | x       | x      | x    | v   | v          | v       | v    | v   |
| PaaS       | x   | x       | x      | x    | x   | x          | x       | v    | v   |
| SaaS       | x   | x       | x      | x    | x   | x          | x       | x    | x   |
```
x - no control
v - control
```