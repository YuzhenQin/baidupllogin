function generatedGid() {
                        return "xxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function(e) {
                            var t = 16 * Math.random() | 0
                                , n = "x" === e ? t : 3 & t | 8;
                            return n.toString(16)
                        }).toUpperCase()
                    }
console.log(generatedGid())