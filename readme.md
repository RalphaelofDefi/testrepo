# Document vs Project — Gap Analysis

**Document:** *"An Intelligent Web-Based Expense Tracker"* (academic project proposal by Richard Raphael Chinonso & Victoria Ihezie, Federal Polytechnic Bida, August 2026)

---

## ✅ What Matches (Implemented)

| Document Requirement | Implementation Status |
|---|---|
| **Three-Tier Architecture** (Presentation / Application / Database) | ✅ Partially — Application + Database layers exist; Presentation (frontend) is a separate client app |
| **PHP 8.2 backend** | ✅ PHP 8.1+ used (`composer.json` requires `>=8.1`) |
| **MySQL database** | ✅ MySQL with full schema, views, foreign keys, indexes |
| **Meta-Llama-3-8B-Instruct via HuggingFace** | ✅ Fully implemented in `AiService.php` + `HuggingFaceService.php` |
| **Authentication Module** (registration, login, session) | ✅ Full auth with registration, login, logout, session management, password hashing (Argon2id) |
| **Transaction Management** (income/expense recording with categories) | ✅ `Transaction` model with CRUD, categories, filters, search, pagination |
| **AI Advisory & Prediction Module** (prompt engineering → LLM) | ✅ `PromptBuilder`, `AIChatService`, `HuggingFaceService` — chat, financial advice, monthly summary |
| **Conversational AI** (natural language queries) | ✅ `/ai/chat` endpoint with chat history and financial context |
| **Security** — Password Hashing, Prepared SQL Statements, Session Management, Input Validation | ✅ All implemented |
| **Analytics & Reporting Module** (financial metrics, summaries) | ✅ `FinanceCalculator` + `MonthlySummaryService` |
| **Database Entities**: User, Transaction, AI Logs, Monthly Summaries | ✅ Tables exist in schema |
| **Data Visualization / Dashboard** | ✅ Backend APIs for dashboard overview and analytics exist |

---

## ❌ What's Missing (Not Implemented)

| Document Requirement | Status | Notes |
|---|---|---|
| **Budget Class / Budgeting Module** | ❌ Missing | Document specifies `Budget` entity with `SetBudget()`, `CheckThreshold()`, `GetVariance()`, category-level budget limits, and **overrun alerts (80%/100%)**. No `Budget` model, no `budgets` table, no budget-related endpoints exist. |
| **Audit Log** | ❌ Missing | Document requires an `Audit Log` entity for tracking system actions. No `audit_logs` table or audit logging mechanism exists. |
| **Spending Prediction / Forecasting** | ❌ Missing | Document explicitly lists "Expense Forecast Report" and "predicted spending estimates." No prediction/forecasting logic exists — only historical summaries and AI-generated advice. |
| **Budget Allocation Form** (user sets per-category monthly limits) | ❌ Missing | No UI or API for defining budget thresholds per category. |
| **Budget Overrun Alerts** (notifications when spending hits 80%/100%) | ❌ Missing | No threshold-checking or alert mechanism for budgets. |
| **UML Class Diagram** classes (Expense, Income, Budget, AIAdvisor as separate entities) | ⚠️ Partially | `Transaction` model combines income+expense (document treats them as separate classes). No `Budget` or `AIAdvisor` classes. |
| **Frontend (Presentation Layer)** | ⚠️ Separate repo | The `.docx` mentions HTML5/CSS3/Bootstrap 5/JavaScript. The frontend lives in `../client/` (separate app). Backend has no views/templates. |
| **Database table `budgets`** | ❌ Missing | Document specifies a `Budget` entity with `BudgetID`, `UserID`, `CategoryID`, `MonthlyLimit`, `MonthYear`. Does not exist in schema. |
| **Database table `audit_logs`** | ❌ Missing | Not in schema. |

---

## ⚠️ Extra Features (Not in Document)

| Feature | Notes |
|---|---|
| **Financial Goals with automated savings deductions** | `goals` table has `scheduled_amount`, `next_deduction_date`, `frequency`, `missed_contributions`. Goal notifications, cron-based auto-deduction. Not mentioned in the document. |
| **OTP verification system** | `user_otps` table + email delivery via PHPMailer. Not in document. |
| **Rate Limiting** | `rate_limits` table + `RateLimitMiddleware`. Not in document. |
| **CSRF Protection** | `CsrfMiddleware`. Not in document. |
| **User Settings** (currency, AI toggle, notification preferences, dashboard preferences) | `user_settings` table. Not in document. |
| **Goal Notifications** | `goal_notifications` table for cron job ↔ frontend. Not in document. |

---

## 📊 Summary

| Category | Count |
|---|---|
| **Fully matching** | ~12 features |
| **Missing from implementation** | ~7 key features (Budget, Audit Log, Forecasting, Budget Alerts) |
| **Extra (not in document)** | ~6 features (Goals with auto-deduction, OTP, Rate Limiting, CSRF, User Settings, Goal Notifications) |

---

## 🔑 Key Verdict

**The project partially matches the document but has significant gaps:**

1. **Budgeting Module is completely absent** — This is a core document requirement. The document specifies `Budget` class, budget thresholds per category, variance calculation, and overrun alerts. None of this exists.
2. **Spending Prediction/Forecasting is missing** — The document emphasizes this as a key differentiator. No prediction logic exists; only historical data summaries.
3. **Audit Logging is missing** — Required for security accountability.
4. **Income is not a separate entity** — Document treats Income and Expense as distinct classes. The project merges them into a single `transactions` table with a `type` field (which is actually a reasonable design choice).

The project has gone beyond the document in some areas (goals, OTP, rate limiting, CSRF, user settings) but has not delivered several core requirements from the proposal.
