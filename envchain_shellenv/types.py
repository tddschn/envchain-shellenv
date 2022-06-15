#!/usr/bin/env python3

ConfigDict = dict[str, dict[str, str | None] | None]
EnvVar = str
EnvchainNamespace = str
EnvchainEnv = str
EnvchainTuple = tuple[EnvVar, EnvchainNamespace, EnvchainEnv]
