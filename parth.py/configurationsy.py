server_ip = ("192.168.1.100",)

allowed_ips = ["192.168.1.10", "192.168.1.20"]

print("--- Initial Server Configuration ---")
print("Server IP (Immutable):", server_ip[0])
print("Allowed IPs (Mutable):", allowed_ips)


print("\n--- Updating Allowed IPs During Runtime ---")
new_ip = "192.168.1.50"
allowed_ips.append(new_ip)
print(f"Added {new_ip} to allowed IPs.")

remove_ip = "192.168.1.10"
if remove_ip in allowed_ips:
  allowed_ips.remove(remove_ip)
  print(f"Removed {remove_ip} from allowed IPs.")

print("Updated Allowed IPs:", allowed_ips)


print("\n--- Attempting to Change Server IP ---")
try:
  server_ip[0] = "10.0.0.1"
except TypeError as e:
  print("Error caught successfully!")
  print("Reason:", e)
  print("Conclusion: server_ip is successfully protected from changes.")