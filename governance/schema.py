"""GovernanceEvent attribute keys (OpenTelemetry span attributes)."""

GOVERNANCE_PREFIX = "governance."
EU_AI_ACT_PREFIX = "eu_ai_act."

EVENT_TYPE = f"{GOVERNANCE_PREFIX}event_type"
AI_SYSTEM_ID = f"{GOVERNANCE_PREFIX}ai_system_id"
SESSION_ID = f"{GOVERNANCE_PREFIX}session_id"
MODEL_ID = f"{GOVERNANCE_PREFIX}model.id"
MODEL_VERSION = f"{GOVERNANCE_PREFIX}model.version"
INPUT_HASH = f"{GOVERNANCE_PREFIX}input_hash"
OUTPUT_HASH = f"{GOVERNANCE_PREFIX}output_hash"
TIMESTAMP_SOURCE = f"{GOVERNANCE_PREFIX}timestamp_source"
REDACTION_APPLIED = f"{GOVERNANCE_PREFIX}redaction_applied"
INTEGRITY_HASH = f"{GOVERNANCE_PREFIX}integrity_hash"

RISK_TIER = f"{EU_AI_ACT_PREFIX}risk_tier"
ANNEX_III_CATEGORY = f"{EU_AI_ACT_PREFIX}annex_iii_category"

TRANSPARENCY_DISCLOSED = f"{GOVERNANCE_PREFIX}transparency.disclosed"
CONTENT_SYNTHETIC = f"{GOVERNANCE_PREFIX}content.synthetic"
