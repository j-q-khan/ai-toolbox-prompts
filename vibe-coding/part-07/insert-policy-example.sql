-- Supabase's own example of a policy for adding rows (an INSERT policy),
-- copied from supabase.com/docs/guides/database/postgres/row-level-security, checked 2026-11-17.
-- It lets signed-in users add a row only when the row's user_id is their own.
-- For reading only: in a Lovable app, ask Lovable to write policies for your own tables
-- (see fix-new-row-prompt.txt). Supabase's docs say to write one policy each for
-- select, insert, update and delete, and to switch Row Level Security on for every table.
create policy "Users can create their own profile."
on profiles for insert
to authenticated
with check ( (select auth.uid()) = user_id );
