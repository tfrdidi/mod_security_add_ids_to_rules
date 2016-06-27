# mod_security_add_ids_to_rules
A small python script that adds ISs to rules of previous version of mod_security that do not have ids yet.

mod_security decided to make IDs mandatory for each role at a certain version. To avoid to add an ID to each role manuall you can use this script. Therefore execuite it with 

```python addModSecurityIDs.py <pathToRuleFile> <firstIDToAssign>```

The script considers ```SecRules```. Only an ID is added if there is no ID is present. Furthermore the chains are considered, meaning only the first rule of a chain gets an ID.


## Example

I want to add IDs to each rules in ```testFile.conf```. The IDs should start with 10000, 10001, ...:
```python addModSecurityIDs.py testFile.conf 10000```

**Input:**
```
SecRule &ARGS "@eq 5" pass,chain,nolog,skipAfter:BLOCK_REQUESTS
        SecRule ARGS_NAMES "^fetch$" chain
        SecRule ARGS_NAMES "^itemType$" chain

SecRule &ARGS "@eq 1" pass,nolog,skipAfter:BLOCK_REQUESTS
```

**Result:**
```
SecRule &ARGS "@eq 5" pass,chain,nolog,skipAfter:BLOCK_REQUESTS,id:10000
        SecRule ARGS_NAMES "^fetch$" chain
        SecRule ARGS_NAMES "^itemType$" chain
        
SecRule &ARGS "@eq 1" pass,nolog,skipAfter:BLOCK_REQUESTS,id:10001
```
