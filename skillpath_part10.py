# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: SkillPath
def case_insensitive_search(records, query, field_keys=None):
    """Perform case-insensitive substring search across specified fields.
    
    Args:
        records: List of dicts to search through.
        query: The search string (case-insensitive).
        field_keys: List of dict keys to search. Defaults to common fields.
        
    Returns:
        List of records where at least one field matches.
    """
    if field_keys is None:
        field_keys = ['goal', 'title', 'description', 'tags', 'resource_name', 
                      'resource_url', 'skill_name', 'category', 'practice_log']
    
    query_lower = query.lower()
    results = []
    
    for record in records:
        for key in field_keys:
            value = record.get(key, '')
            if value and query_lower in str(value).lower():
                results.append(record)
                break
    
    return results
