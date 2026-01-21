-- Fonction d’audit
CREATE OR REPLACE FUNCTION log_action()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO audit_logs (
    user_id,
    action,
    table_name,
    record_id,
    ip_address,
    details
  )
  VALUES (
    auth.uid(),
    TG_OP,
    TG_TABLE_NAME,
    NEW.id,
    inet_client_addr(),
    to_jsonb(NEW)
  );
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Triggers sur accounts
CREATE TRIGGER audit_accounts_update
AFTER UPDATE ON accounts
FOR EACH ROW
EXECUTE FUNCTION log_action();

CREATE TRIGGER audit_accounts_delete
AFTER DELETE ON accounts
FOR EACH ROW
EXECUTE FUNCTION log_action();
