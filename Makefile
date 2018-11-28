set-token:
	sed -i.bak -E 's!YOUR_ROOKOUT_TOKEN!${DEMO_ROOKOUT_TOKEN}!g' serverless.yml