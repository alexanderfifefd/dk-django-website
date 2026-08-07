"""The boundary between external sources and the derived ORM tables.

One module per collection (members, systems, updates, articles). Each holds its
authoring schema, loader, and — where applicable — syncer and ``run_sync_*``
entry point. Management commands are thin wrappers around those.
"""
