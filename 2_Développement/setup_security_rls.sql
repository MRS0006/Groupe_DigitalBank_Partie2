-- 2. ACTIVATION ET CONFIGURATION DU RLS (Tâche 1.2)
------------------------------------------------------------------

-- Activation du RLS sur les tables clés
ALTER TABLE accounts ENABLE ROW LEVEL SECURITY;
ALTER TABLE transactions ENABLE ROW LEVEL SECURITY;

-- Suppression des anciennes politiques pour éviter les erreurs "Already Exists"
DROP POLICY IF EXISTS "Admins : accès complet sur accounts" ON accounts;
DROP POLICY IF EXISTS "Clients : voir uniquement ses comptes" ON accounts;
DROP POLICY IF EXISTS "Admins : accès complet sur transactions" ON transactions;
DROP POLICY IF EXISTS "Analystes : voir toutes les transactions" ON transactions;
DROP POLICY IF EXISTS "Clients : voir ses propres transactions" ON transactions;

--- POLITIQUES SUR LA TABLE : ACCOUNTS ---

-- Admin : Accès total
CREATE POLICY "Admins : accès complet sur accounts" 
ON accounts FOR ALL TO admin_role USING (true);

-- Client : Ne voit que ses comptes (lié à son UID Supabase)
CREATE POLICY "Clients : voir uniquement ses comptes" 
ON accounts FOR SELECT TO authenticated 
USING (customer_id::text = auth.uid()::text);

--- POLITIQUES SUR LA TABLE : TRANSACTIONS ---

-- Admin : Accès total
CREATE POLICY "Admins : accès complet sur transactions" 
ON transactions FOR ALL TO admin_role USING (true);

-- Analyste : Voit tout pour détecter la fraude
CREATE POLICY "Analystes : voir toutes les transactions" 
ON transactions FOR SELECT TO analyst_role USING (true);

-- Client : Voit les transactions de ses comptes uniquement
CREATE POLICY "Clients : voir ses propres transactions" 
ON transactions FOR SELECT TO authenticated 
USING (
  EXISTS (
    SELECT 1 FROM accounts 
    WHERE accounts.account_id = transactions.account_id 
    AND accounts.customer_id::text = auth.uid()::text
  )
);