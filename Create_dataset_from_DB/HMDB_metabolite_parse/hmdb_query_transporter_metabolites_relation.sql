-- Need three tables: metabolites, proteins, metabolite_protein_links 
-- select * from proteins where hmdbp_id = 'HMDBP00446';
-- select * from metabolite_protein_links where protein_id = 5684;

select  name, moldb_smiles, moldb_inchikey from metabolites where id in 
(select metabolite_id from metabolite_protein_links where protein_id = 5684);
