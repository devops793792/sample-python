#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information
#-----------------------------------------------------------------------------------------



@app.route("/")
def hello():
    return app.send_static_file("index.html")
