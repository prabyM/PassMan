from db_handler import create_connection
import pass_object as p

lnt = p.PassObj("lnt.com", "admin", "master")
print (lnt.website)