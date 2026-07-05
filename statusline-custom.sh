#!/bin/bash

# Colors
GREEN='\033[32m'
YELLOW='\033[33m'
RED='\033[31m'
RESET='\033[0m'

# Get model from settings or env
model="${CLAUDE_CODE_MODEL:-haiku}"
model_display="$model"

# Extract JSON from stdin
context_pct="?"
context_pct_num=0
caveman_status="off"
permission_mode="?"

if [ ! -t 0 ]; then
  input=$(cat 2>/dev/null)

  # Extract context usage % (try both possible field names)
  context_pct=$(echo "$input" | jq -r '.context_window.used_percentage // .context_usage_percent // "?"' 2>/dev/null) || context_pct="?"

  # Extract caveman mode (try multiple sources)
  caveman_status=$(echo "$input" | jq -r '.caveman_mode // .harness.caveman_mode // empty' 2>/dev/null)
  if [ -z "$caveman_status" ]; then
    caveman_status="${CAVEMAN_MODE}"
  fi
  # Check marker file
  if [ -z "$caveman_status" ] || [ "$caveman_status" = "off" ]; then
    if [ -f ~/.claude/.caveman-mode-active ]; then
      caveman_status=$(cat ~/.claude/.caveman-mode-active 2>/dev/null)
    fi
  fi
  # Check settings.json for caveman config
  if [ -z "$caveman_status" ] || [ "$caveman_status" = "off" ]; then
    caveman_status=$(jq -r '.caveman.mode // empty' ~/.claude/settings.json 2>/dev/null)
  fi
  # Last resort default
  caveman_status="${caveman_status:-off}"

  # Extract permission mode and cost
  permission_mode=$(echo "$input" | jq -r '.permission_mode // "?"' 2>/dev/null) || permission_mode="?"
  session_cost=$(echo "$input" | jq -r '.cost.total_cost_usd // empty' 2>/dev/null)
  effort_level=$(echo "$input" | jq -r '.effort.level // empty' 2>/dev/null)

  # Get numeric value for color coding
  if [ "$context_pct" != "?" ]; then
    context_pct_num=$(echo "$context_pct" | cut -d'.' -f1)
  fi
fi

# Color context % based on usage
if [ "$context_pct" = "?" ]; then
  context_colored="${context_pct}%"
elif [ "$context_pct_num" -ge 80 ]; then
  context_colored="${RED}${context_pct}%${RESET}"
elif [ "$context_pct_num" -ge 60 ]; then
  context_colored="${YELLOW}${context_pct}%${RESET}"
else
  context_colored="${GREEN}${context_pct}%${RESET}"
fi

# Color caveman status
case "$caveman_status" in
  off) caveman_colored="${RESET}off${RESET}" ;;
  lite) caveman_colored="${YELLOW}lite${RESET}" ;;
  full) caveman_colored="${GREEN}full${RESET}" ;;
  ultra) caveman_colored="${RED}ultra${RESET}" ;;
  *) caveman_colored="${caveman_status}" ;;
esac

# Format permission mode display (full name)
case "$permission_mode" in
  auto) perm_display="auto" ;;
  default) perm_display="default" ;;
  plan) perm_display="plan" ;;
  acceptEdits) perm_display="acceptEdits" ;;
  dontAsk) perm_display="dontAsk" ;;
  *) perm_display="${permission_mode}" ;;
esac

# Color permission mode
if [ "$perm_display" = "?" ]; then
  perm_colored="${perm_display}"
else
  perm_colored="${GREEN}${perm_display}${RESET}"
fi

# Format effort level if present
effort_colored=""
if [ -n "$effort_level" ]; then
  case "$effort_level" in
    low) effort_colored=" ${GREEN}Effort:${effort_level}${RESET}" ;;
    medium) effort_colored=" ${YELLOW}Effort:${effort_level}${RESET}" ;;
    high|max) effort_colored=" ${RED}Effort:${effort_level}${RESET}" ;;
    *) effort_colored=" Effort:${effort_level}" ;;
  esac
fi

# Format cost if present
cost_colored=""
if [ -n "$session_cost" ]; then
  cost_colored=" Cost:\$${session_cost}"
fi

# Format: Model | Mem:NN% | Caveman:X | Effort:X
echo -e "${model_display} | Mem:${context_colored} | Caveman:${caveman_colored}${effort_colored}"
